from Crypto.Cipher import AES
import base64

# Padding function
def pad(text):
    return text + (16 - len(text) % 16) * ' '

def aes_encrypt(key, plaintext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext).encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    return cipher.decrypt(decoded).decode('utf-8').strip()

# Test AES
if __name__ == "__main__":
    key = "thisisakey123456"  # 16-byte key
    text = "Hello, AES Encryption!"
    encrypted = aes_encrypt(key, text)
    
    print("AES Encrypted:", encrypted)
    print("AES Decrypted:", aes_decrypt(key, encrypted))
