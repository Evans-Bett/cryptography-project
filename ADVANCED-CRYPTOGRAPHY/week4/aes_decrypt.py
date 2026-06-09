from Crypto.Cipher import AES

with open("aes_key.txt", "r") as f:
    key = bytes.fromhex(f.read())

with open("encrypted.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print("Decrypted Message:")
print(plaintext.decode())