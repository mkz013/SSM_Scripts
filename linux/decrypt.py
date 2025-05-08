import os
from Crypto.Cipher import AES
from hashlib import sha256

password = "happy"
AES_KEY = sha256(password.encode()).digest()[:16]

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def decrypt_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            iv = file.read(16)  encrypted_content = file.read()  

        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
        original_content = unpad(cipher.decrypt(encrypted_content))  

        
        with open(file_path, 'wb') as file:
            file.write(original_content)

        print(f"🔓 Decrypted: {file_path}")
        print("🎉 Your files have been rescued! All back to normal. 😊")

    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")

# Decrypt all files
files = [
    r"C:\Users\ochis\Desktop\Personal FIles\images.png",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.txt",
    r"C:\Users\ochis\Desktop\Personal FIles\dummy.pdf"
]

for file_path in files:
    decrypt_file(file_path)
