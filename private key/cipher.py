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
	def generate_key(key, n):
		m = len(key)
		new_key = key*(n//m)
		for i in range(n%m):
			new_key += key[i]
		return new_key

	@staticmethod
	def encrypt(plaintext, key):
		plaintext = plaintext.lower()
		key = key.lower()
		key = VignereCipher.generate_key(key, len(plaintext))
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
		key = VignereCipher.generate_key(key, len(ciphertext))
		plaintext = []
		for i in range(len(ciphertext)):
			c = alph2idx[ciphertext[i]]
			k = alph2idx[key[i]]
			p = (c-k+26)%26
			plaintext.append(idx2alph[p])
		return "".join(plaintext)