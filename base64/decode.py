import base64
import os

def decrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            encrypted_content = file.read()
        
        original_content = base64.b64decode(encrypted_content)
        
        with open(file_path, 'wb') as file:
            file.write(original_content)
        
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")

# List of files to decrypt
files_to_decrypt = [
    r"C:\Users\ochis\Desktop\Personal FIles\images.png",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.txt",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.pdf"
]

for file_path in files_to_decrypt:
    decrypt_file(file_path)
