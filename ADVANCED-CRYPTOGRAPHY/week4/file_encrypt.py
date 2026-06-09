from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data_text = "This file contains confidential information for AES encryption testing."

with open("sample.txt", "w") as f:
    f.write(data_text)

print("Sample file created successfully.")

with open("sample.txt", "rb") as f:
    data = f.read()

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted.bin", "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(ciphertext)

print("\nEncryption Successful!")
print("AES Key (SAVE THIS):", key.hex())
print("Encrypted file created: encrypted.bin")