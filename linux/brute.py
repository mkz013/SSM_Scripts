import os
from Crypto.Cipher import AES
from hashlib import sha256

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def is_valid_plaintext(data):
    try:
        decoded = data.decode('utf-8')
        return "howest" in decoded.lower()  # Customize this if you know any content
    except UnicodeDecodeError:
        return False

def try_password(file_path, password):
    try:
        key = sha256(password.encode()).digest()[:16]
        with open(file_path, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted)

        if is_valid_plaintext(decrypted):
            print(f"\n✅ Correct password found: '{password}'")
            return True
        return False
    except Exception:
        return False

def brute_force_aes(file_path, wordlist_path):
    with open(wordlist_path, 'r', encoding='latin-1') as wordlist:
        for line in wordlist:
            password = line.strip()
            print(f"Trying: {password}")
            if try_password(file_path, password):
                return
    print("\n❌ Password not found in the wordlist.")

# Adjust paths
encrypted_file_path = "/home/dudekszymon/UCDP/testFile.txt"
wordlist_path = "/home/dudekszymon/UCDP-Rans/rockyou.txt"

brute_force_aes(encrypted_file_path, wordlist_path)
