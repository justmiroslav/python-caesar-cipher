def encrypt(raw_text, key):
    encrypted_text = ""
    for char in raw_text:
        if char.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz" if char.islower() else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            encrypted_text += alphabet[(ord(char) - ord("a" if char.islower() else "A") + key + 26) % 26]
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(raw_text, key):
    return encrypt(raw_text, -key)


text = encrypt("Hello, world!", 11134)
print(text)
print(decrypt(text, 11134))
