def encrypt_caesar_cipher(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(ciphertext, shift):
    return encrypt_caesar_cipher(ciphertext, -shift)

def main():
    print("Caesar Cipher Program")
    action = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if action not in ('E', 'D'):
        print("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")
        return

    text = input("Enter the text: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if action == 'E':
        result = encrypt_caesar_cipher(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt_caesar_cipher(text, shift)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
