def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                # Shift lowercase letters
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # If character is not a letter, leave it unchanged
            result += char
    return result


text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)
