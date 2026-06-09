from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

message = b"Secure File Sharing System Using RSA"

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("rsa_encrypted.bin", "wb") as f:
    f.write(ciphertext)

print("Message Encrypted Successfully")
print("Ciphertext (sample):", ciphertext[:30])