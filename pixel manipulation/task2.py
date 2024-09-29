from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Apply basic mathematical operations to each pixel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Reverse the mathematical operations to decrypt
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

def main():
    print("Simple Image Encryption Tool")
    while True:
        choice = input("\nChoose an option:\n1. Encrypt Image\n2. Decrypt Image\n3. Exit\nEnter your choice: ")
        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, key)
        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_path, key)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
