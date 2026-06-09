import time

def simple_encrypt(data):
    return [ord(c) ^ 5 for c in data]


data = "HI EVERYONE"

start = time.time()
encrypted = simple_encrypt(data)
end = time.time()

print("Encrypted Data:", encrypted)
print("Time taken:", end - start, "seconds")