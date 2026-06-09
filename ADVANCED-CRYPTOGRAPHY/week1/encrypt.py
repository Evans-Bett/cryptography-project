from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Sample data
data = b"Hello, this is a test message for encryption"

# Generate key
key = get_random_bytes(16)

# Create cipher
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt data
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Original Data:", data)
print("Encrypted Data:", ciphertext)
print("Key:", key)
print("Nonce:", cipher.nonce)