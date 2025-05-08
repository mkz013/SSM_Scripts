import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256  # Used to convert password into AES key

# Convert password into a 16-byte AES key (SHA-256 hash and truncate)
password = "happy"
AES_KEY = sha256(password.encode()).digest()[:16]  # Use first 16 bytes

# Function to pad data to be a multiple of AES block size (16 bytes)
def pad(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

# Function to remove padding
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# AES Encryption function with a playful message
def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            original_content = file.read()

        iv = get_random_bytes(16)  # Generate a random IV
        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
        encrypted_content = cipher.encrypt(pad(original_content))  # Encrypt with padding

        # Save the IV + encrypted content
        with open(file_path, 'wb') as file:
            file.write(iv + encrypted_content)

        # Playful message
        print(f"🔒 Encrypted: {file_path}")
        print("🎉 Your files are now safely locked away! Don't worry, they're just taking a little nap. 💤")

    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")


# List of files to encrypt/decrypt
files = [
    r"/home/dudekszymon/UCDP/testFile.txt",
    r"/home/dudekszymon/UCDP/Flowers.jpg"
]

# Encrypt all files
for file_path in files:
    encrypt_file(file_path)
