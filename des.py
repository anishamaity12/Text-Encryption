from Crypto.Cipher import DES
import base64

# Padding function
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(key, plaintext):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext).encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def des_decrypt(key, ciphertext):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    return cipher.decrypt(decoded).decode('utf-8').strip()

# Test DES
if __name__ == "__main__":
    key = "8bytekey"  # DES key must be 8 bytes
    text = "Hello, DES Encryption!"
    encrypted = des_encrypt(key, text)
    print("DES Encrypted:", encrypted)
    print("DES Decrypted:", des_decrypt(key, encrypted))
