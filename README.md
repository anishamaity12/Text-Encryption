# Text-Encryption
## Description
This project demonstrates the implementation of various encryption algorithms for secure text communication. It includes:

- **AES (Advanced Encryption Standard):** A secure symmetric encryption technique.
- **DES (Data Encryption Standard):** An older symmetric encryption method.
- **RSA:** An asymmetric encryption method using public and private keys.

The program allows users to encrypt and decrypt text using these algorithms, providing a hands-on understanding of encryption techniques.

## Features
- Encrypt text using AES, DES, or RSA algorithms.
- Decrypt the encrypted text to retrieve the original message.
- Menu-driven interface for ease of use.
- Supports:
  - 16-byte AES keys
  - 8-byte DES keys
  - RSA key generation and usage.

## Requirements
- Libraries:
  - `cryptography`
  - `pycryptodome`

### Installation
Run the following command to install the required libraries:
```bash
pip install cryptography pycryptodome
