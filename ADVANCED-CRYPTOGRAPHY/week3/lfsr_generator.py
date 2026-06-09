def lfsr(seed, taps, length):
    state = seed
    result = []

    for _ in range(length):
        xor = 0
        for t in taps:
            xor ^= state[t]

        result.append(state[-1])
        state = [xor] + state[:-1]

    return result


seed = [1, 0, 0, 1]
taps = [0, 3]

output = lfsr(seed, taps, 10)
print("LFSR Output:", output)