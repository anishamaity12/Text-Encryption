from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt_decrypt():
    # Generate RSA key pair
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    
    plaintext = "Hello, RSA Encryption!"
    encrypted = cipher.encrypt(plaintext.encode('utf-8'))
    print("RSA Encrypted:", encrypted)

    # Decrypt
    decipher = PKCS1_OAEP.new(key)
    decrypted = decipher.decrypt(encrypted)
    print("RSA Decrypted:", decrypted.decode('utf-8'))

if __name__ == "__main__":
    rsa_encrypt_decrypt()
