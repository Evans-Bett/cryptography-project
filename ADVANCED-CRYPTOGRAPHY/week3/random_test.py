import random

sequence = [random.randint(0, 1) for _ in range(100)]

zeros = sequence.count(0)
ones = sequence.count(1)

print("Total bits:", len(sequence))
print("Zeros:", zeros)
print("Ones:", ones)

if abs(zeros - ones) < 10:
    print("Sequence is fairly random")
else:
    print("Sequence is NOT random enough")