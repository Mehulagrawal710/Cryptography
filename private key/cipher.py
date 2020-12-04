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


key = 10
enc_msg = CaesarCipher.encrypt("mehul agrawal", key)
dec_msg = CaesarCipher.decrypt(enc_msg, key)
print(enc_msg, dec_msg)
print()
CaesarCipher.bruteForceAttack(enc_msg)