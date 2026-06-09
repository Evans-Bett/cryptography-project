def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    j = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            j += 1
        else:
            result += char

    return result


message = "HELLO MR. Nyoro"
key = "key"

print("Original:", message)
print("Encrypted:", vigenere_encrypt(message, key))