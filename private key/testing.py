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

print("------Playfair Cipher:------")
plaintext = "PASSIVE ATTACK IS STILL BAD"
key = "PROGRAMMING"
enc_msg = PlayfairCipher.encrypt(plaintext, key)
dec_msg = PlayfairCipher.decrypt(enc_msg, key)
print(plaintext, "=>", enc_msg, "=>",dec_msg)