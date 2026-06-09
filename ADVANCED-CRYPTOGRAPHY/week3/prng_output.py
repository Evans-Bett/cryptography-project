import random

random.seed(42)

sequence = [random.randint(0, 1) for _ in range(20)]

print("Pseudorandom Sequence Output:")
print(sequence)