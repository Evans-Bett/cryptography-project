def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    j = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - base) % 26 + base)
            j += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    j = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - base) % 26 + base)
            j += 1
        else:
            result += char
    return result


message = "I AM A KENYAN"
key = "key"

encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)