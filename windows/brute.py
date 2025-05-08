import os
from Crypto.Cipher import AES
from hashlib import sha256

# Function to unpad the decrypted data
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Function to check if the decrypted content is valid (PDF header)
def is_valid_pdf(decrypted_content):
    return decrypted_content.startswith(b'%PDF')

# AES decryption attempt using a given password
def decrypt_file_with_password(file_path, password):
    try:
        # Derive AES key from password
        AES_KEY = sha256(password.encode()).digest()[:16]  # Truncate to 16 bytes

        with open(file_path, 'rb') as file:
            iv = file.read(16)  # Read the first 16 bytes (IV)
            encrypted_content = file.read()  # The rest is the encrypted content

        # Decrypt the content
        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
        decrypted_content = cipher.decrypt(encrypted_content)
        decrypted_content = unpad(decrypted_content)

        # Check if the decrypted content is a valid PDF
        if is_valid_pdf(decrypted_content):
            # Save the decrypted content if it's valid
            with open(f"decrypted_{os.path.basename(file_path)}", 'wb') as decrypted_file:
                decrypted_file.write(decrypted_content)
            return True  # Decryption succeeded
        else:
            print(f"Failed to decrypt with password: {password}")
            return False  # Decryption failed (invalid content)

    except (ValueError, KeyError, Exception) as e:
        # If there's a decryption error, it means the password is incorrect or padding is wrong
        print(f"Error decrypting with password '{password}': {e}")
        return False

# Brute-force with a wordlist
def brute_force_decrypt(file_path, wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()  # Remove any surrounding whitespace/newlines
            print(f"Trying password: {password}")
            if decrypt_file_with_password(file_path, password):
                print(f"Decryption succeeded with password: {password}")
                break  # Stop if we successfully decrypt the file
        else:
            print("Decryption failed. No passwords from the wordlist worked.")

# Define paths -> Adjust as needed 
encrypted_file_path = r"C:\Users\ochis\Desktop\Personal FIles\dummy.pdf"  # Path to the encrypted file
wordlist_path = r"C:\Users\ochis\Desktop\wordlist.txt"  # Path to your wordlist

# Brute-force decrypt the file
brute_force_decrypt(encrypted_file_path, wordlist_path)
