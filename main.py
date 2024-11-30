from aes import aes_encrypt, aes_decrypt
from des import des_encrypt, des_decrypt
from rsa import rsa_encrypt_decrypt

def main():
    print("Text Encryption Project")
    print("1. AES Encryption")
    print("2. DES Encryption")
    print("3. RSA Encryption/Decryption")
    print("4. Exit")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        key = input("Enter a 16-byte AES key: ")
        text = input("Enter the text to encrypt: ")
        encrypted = aes_encrypt(key, text)
        print("Encrypted Text:", encrypted)
        print("Decrypted Text:", aes_decrypt(key, encrypted))
    
    elif choice == 2:
        key = input("Enter an 8-byte DES key: ")
        text = input("Enter the text to encrypt: ")
        encrypted = des_encrypt(key, text)
        print("Encrypted Text:", encrypted)
        print("Decrypted Text:", des_decrypt(key, encrypted))
    
    elif choice == 3:
        rsa_encrypt_decrypt()
    
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
