def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Tool")
    while True:
        choice = input("\nChoose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice: ")
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print("Encrypted Text:", encrypted_text)
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print("Decrypted Text:", decrypted_text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
