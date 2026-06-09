from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

message = input("Enter message to send securely: ").encode()

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Secure Message Sent (Encrypted):", encrypted)