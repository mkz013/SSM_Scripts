import base64
import os

def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            original_content = file.read()
        
        encrypted_content = base64.b64encode(original_content)
        
        with open(file_path, 'wb') as file:
            file.write(encrypted_content)
        
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

# List of files to encrypt
files_to_encrypt = [
    r"C:\Users\ochis\Desktop\Personal FIles\images.png",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.txt",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.pdf"
]

for file_path in files_to_encrypt:
    encrypt_file(file_path)
