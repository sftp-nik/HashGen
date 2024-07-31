# HashGen

## Overview

Folder Hash Generator is a Python script that calculates the SHA-256 hash of a folder. This can be useful for verifying the integrity of the contents within a folder. The script processes each file within the folder, generates a SHA-256 hash for each file, and then combines these hashes to produce a single SHA-256 hash for the entire folder.

## Features

- Generates SHA-256 hash for individual files.
- Generates SHA-256 hash for an entire folder by combining the hashes of individual files.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sftp-nik/HashGen.git
```

2. Navigate to the project directory:

```bash
cd HashGen
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Enter the path of the folder you want to hash when prompted:

```bash
Enter Folder Path: /path/to/your/folder
```

3. The script will output the SHA-256 hash of the folder.

## Example

```bash
$ python hash_folder.py
Enter Folder Path: /path/to/your/folder
The hash of the folder is: <calculated_hash>
Developed by Nik
```

## Script Explanation

The script consists of two main functions:

1. **`hash_file(file_path)`**: This function generates the SHA-256 hash for an individual file.
2. **`hash_folder(folder_path)`**: This function generates the SHA-256 hash for a folder by iterating through all the files in the folder, generating their hashes, and then combining these hashes to produce a single SHA-256 hash for the folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Developed By

Nik
