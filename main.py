import re


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


def read_file(filename, start, end):
    try:
        with open(filename, "r") as file:
            content = file.read()
            if start < 0 or start >= end or end > len(content):
                raise "Invalid boundaries"
            print("Text has been loaded successfully")
            return content[start-1:end-1] if start > 0 else content[start:end]
    except Exception as e:
        raise f"Error: {e}"


def write_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)
        print("Text has been saved successfully")


def main():
    while True:
        user_input = int(input("Enter 1 to encrypt the text/2 to decrypt the text/3 to stop the program: "))
        if user_input == 1 or user_input == 2:
            load_file = input("Enter the filename for loading: ")
            boundaries = re.split(r"[,\s]+", input("Enter the start and end boundaries: "))
            try:
                file_text = read_file(load_file, int(boundaries[0]), int(boundaries[1]))
                write_file_name = input("Enter the filename for saving: ")
                try:
                    key = int(input("Enter encryption key: " if user_input == 1 else "Enter decryption key: "))
                    processed_text = encrypt(file_text, key) if user_input == 1 else decrypt(file_text, key)
                    write_file(write_file_name, processed_text)
                except Exception as e:
                    print("Error:", e)
            except Exception as e:
                print("Error:", e)
        elif user_input == 3:
            print("Program stopped")
            break
        else:
            print("Enter a valid command")


if __name__ == "__main__":
    main()
