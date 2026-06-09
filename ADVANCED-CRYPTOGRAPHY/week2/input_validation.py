text = input("Enter message: ")
key = input("Enter key: ")

if len(text.strip()) == 0:
    print("❌ Error: Message cannot be empty")

elif len(key.strip()) < 2:
    print("❌ Error: Key must be at least 2 characters")

elif not key.isalpha():
    print("❌ Error: Key must contain only letters")

else:
    print("✅ Valid input. Processing encryption...")

    # Simple Caesar preview (optional)
    shift = 3
    encrypted = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    print("Encrypted Preview:", encrypted)