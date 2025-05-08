import os
import random
import argparse

def corrupt_file(file_path, corruption_percentage=10):
    """Corrupt a file by randomly modifying a percentage of its content"""
    try:
        # Read the file
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())
        
        if not data:
            print(f"Skipping empty file: {file_path}")
            return False
            
        # Calculate how many bytes to corrupt
        bytes_to_corrupt = max(1, int(len(data) * corruption_percentage / 100))
        
        # Corrupt random bytes
        for _ in range(bytes_to_corrupt):
            position = random.randint(0, len(data) - 1)
            data[position] = random.randint(0, 255)
        
        # Write back the corrupted data
        with open(file_path, 'wb') as f:
            f.write(data)
            
        print(f"Corrupted {bytes_to_corrupt} bytes in {file_path}")
        return True
    
    except Exception as e:
        print(f"Failed to corrupt {file_path}: {e}")
        return False

def corrupt_directory(directory, corruption_percentage=10, file_extensions=None):
    """Corrupt files in a directory with specified extensions"""
    corrupted_files = 0
    failed_files = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if we should process this file extension
            if file_extensions and not any(file.endswith(ext) for ext in file_extensions):
                continue
                
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                if corrupt_file(file_path, corruption_percentage):
                    corrupted_files += 1
                else:
                    failed_files += 1
    
    print(f"Corruption complete: {corrupted_files} files corrupted, {failed_files} failed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Corruption Simulation")
    parser.add_argument("target", help="Directory or file to corrupt")
    parser.add_argument("--percentage", type=float, default=10, 
                        help="Percentage of file content to corrupt (1-100)")
    parser.add_argument("--extensions", nargs='+', 
                        help="File extensions to target (e.g., .docx .pdf .jpg)")
    args = parser.parse_args()
    
    if os.path.isdir(args.target):
        print(f"WARNING: This will corrupt files in {args.target}")
        confirm = input("Type 'YES' to continue: ")
        if confirm == "YES":
            corrupt_directory(args.target, args.percentage, args.extensions)
        else:
            print("Operation cancelled")
    elif os.path.isfile(args.target):
        print(f"WARNING: This will corrupt {args.target}")
        confirm = input("Type 'YES' to continue: ")
        if confirm == "YES":
            corrupt_file(args.target, args.percentage)
        else:
            print("Operation cancelled")
    else:
        print(f"Error: {args.target} is not a valid file or directory")