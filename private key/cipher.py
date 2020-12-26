import math
from helper import *

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
		ciphertext = ciphertext.lower()
		for key in range(26):
			print("key({}): {}".format(key, CaesarCipher.decrypt(ciphertext, key)))

class MonoAlphabeticCipher():
	@staticmethod
	def encrypt(plaintext, mapping):
		ciphertext = []
		for words in plaintext.split():
			for letter in words:
				ciphertext.append(mapping[letter])
		return "".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, mapping):
		rev_mapping = {v: k for k, v in mapping.items()}
		plaintext = []
		for letter in ciphertext:
				plaintext.append(rev_mapping[letter])
		return "".join(plaintext)

#polyalphabetic
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

# class HillCipher():
# 	@staticmethod
# 	def encrypt(plaintext, key):
# 		m = len(key)
# 		plaintext = plaintext.lower()
# 		key = numpy.array(key)
# 		print("key:")
# 		print(key)
# 		ciphertext = []
# 		for i in range(len(plaintext)//m):
# 			p_vec = numpy.zeros(shape=(1,m))
# 			for j in range(m):
# 				p_vec[0][j] = alph2idx[plaintext[m*i+j]]
# 			print("p vec=>", p_vec)
# 			c_vec = numpy.dot(p_vec, key)
# 			print("c vec=>", c_vec, end = ", ")
# 			c_vec = c_vec%26
# 			print(c_vec)
# 			for x in c_vec[0]:
# 				ciphertext.append(idx2alph[x])
# 		return "".join(ciphertext)

# 	@staticmethod
# 	def decrypt(ciphertext, key):
# 		m = len(key)
# 		key = modMatInv(key, 26)
# 		print("key:")
# 		print(key)
# 		plaintext = []
# 		for i in range(len(ciphertext)//m):
# 			c_vec = numpy.zeros(shape=(1,m))
# 			for j in range(m):
# 				c_vec[0][j] = alph2idx[ciphertext[m*i+j]]
# 			print("c vec=>", c_vec)
# 			p_vec = numpy.dot(c_vec, key)
# 			print("p vec=>", p_vec, end = ", ")
# 			p_vec = c_vec%26
# 			print(p_vec)
# 			for x in p_vec[0]:
# 				plaintext.append(idx2alph[x])
# 		return "".join(plaintext)


# Transposition Techniques
class RailFenceCipher():
	@staticmethod
	def encrypt(plaintext, depth):
		plaintext = plaintext.lower()
		plaintext = "".join(plaintext.split())
		n = len(plaintext)
		ciphertext = []
		for d in range(depth):
			for i in range(math.ceil(n/depth)):
				if i*depth+d < n:
					ciphertext.append(plaintext[i*depth+d])
		return "".join(ciphertext)

	@staticmethod
	def decrypt(ciphertext, depth):
		n = len(ciphertext)
		plaintext = []
		c = math.ceil(n/depth)
		for i in range(c):
			for d in range(depth):
				if d*c+i < n:
					plaintext.append(ciphertext[d*c+i])
		return "".join(plaintext)

class ColumnarCipher():
	@staticmethod
	def encrypt(plaintext, key):
		pass

	@staticmethod
	def decrypt(ciphertext, key):
		pass

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