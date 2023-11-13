import pyAesCrypt


def encryption(not_enc_file='encrypt/file.txt', enc_file='enc_file.txt', pwd = '123'):
   pyAesCrypt.encryptFile(not_enc_file, enc_file, pwd)
     

def decryption(ready_enc_file='decrypt/file.txt', decrypt_file='dec_result/', pwd = '123'):
   pyAesCrypt.decryptFile(ready_enc_file, decrypt_file, pwd)
   