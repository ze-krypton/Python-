from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = input("Enter key: ").encode()
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

plaintext = input("Enter message: ").encode()
padded_text = pad(plaintext, Blowfish.block_size)

ciphertext = cipher.encrypt(padded_text)
print("\nEncrypted message:", ciphertext.hex())

decrypted = cipher.decrypt(ciphertext)
print("Decrypted message:", unpad(decrypted, Blowfish.block_size).decode())
