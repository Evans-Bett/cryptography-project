def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


test_cases = [
    "HELLO",
    "ATTACK",
    "SECURITY",
    "CRYPTOGRAPHY"
]

shift = 3

print("Cipher Testing Results:\n")

for text in test_cases:
    print("Original:", text, "→ Encrypted:", caesar(text, shift))