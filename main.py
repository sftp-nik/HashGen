import os
import hashlib

def hash_file(file_path):         # to genrate hash for file
#   Generate SHA-256 hash of a file.
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except IOError:
        return None

def hash_folder(folder_path):   # to genrate has for folder
#   Generate SHA-256 hash for a folder
    sha256 = hashlib.sha256()
    for root, _, files in sorted(os.walk(folder_path)):
        for name in sorted(files):
            file_path = os.path.join(root, name)
            file_hash = hash_file(file_path)
            if file_hash:
                
                sha256.update(file_hash.encode('utf-8'))
    return sha256.hexdigest()

folder_path = input("Enter Folder Path: ")  # folder path
folder_hash = hash_folder(folder_path)
print(f'The hash of the folder is: {folder_hash}')
print("Developed by Nik")

