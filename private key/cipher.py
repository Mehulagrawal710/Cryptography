idx2alph = {i: chr(ord('a')+i) for i in range(26)}
alph2idx = {y: x for x, y in idx2alph.items()}

class CaesarCipher():
	@staticmethod
	def encrypt(plaintext, key):
		plaintext = plaintext.lower()
		ciphertext = []
		for word in plaintext.split():
			s = ""
			for x in word:
				shifted_idx = (alph2idx[x]+key)%26
				s = s + idx2alph[shifted_idx]
			ciphertext.append(s)
		return " ".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, key):
		plaintext = []
		for word in ciphertext.split():
			s = ""
			for x in word:
				shifted_idx = (alph2idx[x]-key+26)%26
				s = s + idx2alph[shifted_idx]
			plaintext.append(s)
		return " ".join(plaintext)

	@staticmethod
	def bruteForceAttack(ciphertext):
		for key in range(26):
			print("key({}): {}".format(key, CaesarCipher.decrypt(ciphertext, key)))

class VernamCipher():
	@staticmethod
	def encrypt(plaintext, key):
		if len(key)!=len(plaintext):
			raise Exception("Key length should be same as of plaintext")
		plaintext = plaintext.lower()
		key = key.lower()
		ciphertext = []
		for i in range(len(plaintext)):
			p = alph2idx[plaintext[i]]
			k = alph2idx[key[i]]
			c = p+k
			if c >= 26: c -= 26
			ciphertext.append(idx2alph[c])
		return "".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, key):
		if len(key)!=len(ciphertext):
			raise Exception("Key length should be same as of ciphertext")
		key = key.lower()
		plaintext = []
		for i in range(len(ciphertext)):
			c = alph2idx[ciphertext[i]]
			k = alph2idx[key[i]]
			p = c-k
			if p < 0: p += 26
			plaintext.append(idx2alph[p])
		return "".join(plaintext)

class VignereCipher():
	@staticmethod
	def generateKey(key, n):
		m = len(key)
		new_key = key*(n//m)
		for i in range(n%m):
			new_key += key[i]
		return new_key

	@staticmethod
	def encrypt(plaintext, key):
		plaintext = plaintext.lower()
		key = key.lower()
		key = VignereCipher.generateKey(key, len(plaintext))
		ciphertext = []
		for i in range(len(plaintext)):
			p = alph2idx[plaintext[i]]
			k = alph2idx[key[i]]
			c = (p+k)%26
			ciphertext.append(idx2alph[c])
		return "".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, key):
		key = key.lower()
		key = VignereCipher.generateKey(key, len(ciphertext))
		plaintext = []
		for i in range(len(ciphertext)):
			c = alph2idx[ciphertext[i]]
			k = alph2idx[key[i]]
			p = (c-k+26)%26
			plaintext.append(idx2alph[p])
		return "".join(plaintext)

class PlayfairCipher():
	@staticmethod
	def generatePairs(plaintext):
		pairs = [[None, None]]
		i = 0
		while i < len(plaintext):
			if pairs[-1][0] is None:
				pairs[-1][0] = plaintext[i]
				i += 1
			elif pairs[-1][1] is None:
				if pairs[-1][0] == plaintext[i]:
					pairs[-1][1] = 'x'
				else:
					pairs[-1][1] = plaintext[i]
					i += 1
			else:
				pairs.append([None, None])
		if pairs[-1][1] is None:
			pairs[-1][1] = 'x'
		return pairs

	@staticmethod
	def generateKeyMatrix(key):
		keymap = {k: None for k in alph2idx.keys()}
		r = 0
		c = 0
		for x in key:
			if x=='j': x = 'i'
			if keymap[x] is None:
				keymap[x] = [r, c]
				c += 1
				if c>=5:
					r += 1
					c = 0
		for k in keymap.keys():
			if k=='j': k = 'i'
			if keymap[k] is None:
				keymap[k] = [r, c]
				c += 1
				if c>=5:
					r += 1
					c = 0
		keymap['j'] = keymap['i']
		mat = [[None for i in range(5)] for j in range(5)]
		for k, v in keymap.items():
			r, c = v
			mat[r][c] = k
		mat[keymap['i'][0]][keymap['i'][1]] = 'i'
		return keymap, mat

	@staticmethod
	def encrypt(plaintext, key):
		plaintext = plaintext.lower()
		key = key.lower()
		plaintext = "".join(plaintext.split())
		pairs = PlayfairCipher.generatePairs(plaintext)
		keymap, keymatrix = PlayfairCipher.generateKeyMatrix(key)
		ciphertext = []
		for pair in pairs:
			r1, c1 = keymap[pair[0]]
			r2, c2 = keymap[pair[1]]
			if r1==r2:
				cphrt = keymatrix[r1][(c1+1)%5] + keymatrix[r2][(c2+1)%5]
			elif c1==c2:
				cphrt = keymatrix[(r1+1)%5][c1] + keymatrix[(r2+1)%5][c2]
			else:
				cphrt = keymatrix[r1][c2] + keymatrix[r2][c1]
			ciphertext.append(cphrt)
		return "".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, key):
		key = key.lower()
		pairs = PlayfairCipher.generatePairs(ciphertext)
		keymap, keymatrix = PlayfairCipher.generateKeyMatrix(key)
		plaintext = []
		for pair in pairs:
			r1, c1 = keymap[pair[0]]
			r2, c2 = keymap[pair[1]]
			if r1==r2:
				plnt = keymatrix[r1][(c1-1+5)%5] + keymatrix[r2][(c2-1+5)%5]
			elif c1==c2:
				plnt = keymatrix[(r1-1+5)%5][c1] + keymatrix[(r2-1+5)%5][c2]
			else:
				plnt = keymatrix[r1][c2] + keymatrix[r2][c1]
			plaintext.append(plnt)
		return "".join(plaintext)