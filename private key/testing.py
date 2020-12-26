from cipher import *

print("------Caesar Cipher:------")
plaintext = "mehul agrawal"
key = 10
enc_msg = CaesarCipher.encrypt(plaintext, key)
dec_msg = CaesarCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)
CaesarCipher.bruteForceAttack(enc_msg)

print("------Vernam Cipher:------")
plaintext = "Mehul"
key = "hello"
enc_msg = VernamCipher.encrypt(plaintext, key)
dec_msg = VernamCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)

print("------Vignere Cipher:------")
plaintext = "VignereCipher"
key = "mehul"
enc_msg = VignereCipher.encrypt(plaintext, key)
dec_msg = VignereCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)

print("------MonoAlphabeticCipher Cipher:------")
plaintext = "it was disclosed yesterday that several informal but direct contacts have been made with political representatives of the viet cong in moscow"
key = {
'a': 'h',
'b': 'y',
'c': 'e',
'd': 'n',
'e': 'c',
'f': 'q',
'g': 'r',
'h': 's',
'i': 't',
'j': 'i', 
'k': 'o', 
'l': 'd', 
'm': 'l', 
'n': 'j',
'o': 'x', 
'p': 'u', 
'q': 'a', 
'r': 'z', 
's': 'm', 
't': 'b', 
'u': 'k',
'v': 'w', 
'w': 'v', 
'x': 'g', 
'y': 'f', 
'z': 'p'}
enc_msg = MonoAlphabeticCipher.encrypt(plaintext, key)
dec_msg = MonoAlphabeticCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)

print("------Playfair Cipher:------")
plaintext = "PASSIVE ATTACK IS STILL BAD"
key = "PROGRAMMING"
enc_msg = PlayfairCipher.encrypt(plaintext, key)
dec_msg = PlayfairCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)

# print("------Hill Cipher:------")
# plaintext = "paymoremoney"
# key = [[17, 17, 5],
#        [21, 18, 21],
#        [2, 2, 19]]
# enc_msg = HillCipher.encrypt(plaintext, key)
# dec_msg = HillCipher.decrypt(enc_msg, key)
# print(plaintext, "=>", enc_msg, "=>",dec_msg)

