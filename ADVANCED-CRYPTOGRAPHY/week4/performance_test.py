import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"A" * 1000000

key = get_random_bytes(16)

start = time.time()

cipher = AES.new(key, AES.MODE_EAX)
cipher.encrypt(data)

end = time.time()

print("AES Encryption Time:")
print(end - start, "seconds")