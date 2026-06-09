def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char

    return encrypted


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

result = caesar_encrypt(message, shift)

print("Original:", message)
print("Encrypted:", result)