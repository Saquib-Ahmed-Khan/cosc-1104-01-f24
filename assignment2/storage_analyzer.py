# storage_analyzer.py
# Author: Saquib Ahmed Khan-100949697
# Date: 15 November 2024
# Description: A Python program that analyzes a folder's storage by categorizing files by type, detecting duplicates, and identifying the top largest files. It helps users optimize storage usage efficiently.


import os  # Used to work with files and folders, such as checking their size or navigating directories.
import hashlib  # Helps create unique codes (hashes) for each file to detect duplicates.

def get_file_extension(file_path):
    """
    Finds the type of a file by its extension (e.g., .txt, .jpg).
    Useful for grouping files by type.
    """
    return os.path.splitext(file_path)[1].lower()  # Extracts the part after the last dot in the file name.

def calculate_file_hash(file_path):
    """
    Creates a unique code (SHA256 hash) for a file to detect duplicates.
    Even if files have the same name, this compares their actual content.
    """
    hasher = hashlib.sha256()  # SHA256 is chosen for its reliability in creating unique codes.
    with open(file_path, 'rb') as file:  # Files are opened in binary mode to handle all types of files.
        while chunk := file.read(8192):  # Reading files in small chunks is memory-efficient, especially for large files.
            hasher.update(chunk)  # Updates the hash value with each chunk of the file.
    return hasher.hexdigest()  # Returns the computed hash as a text string.

def analyze_storage(folder_path):
    """
    Analyzes all files in a folder:
    - Groups files by their type.
    - Finds duplicate files based on their content.
    - Lists the top 5 largest files.
    """
    file_types = {}  # Tracks the total size of each file type (e.g., .txt, .jpg).
    duplicate_files = {}  # Stores files that are exactly the same based on their content hash.
    file_sizes = []  # Keeps a record of all files and their sizes.

    # Walk through the directory structure, processing each file.
    for root, _, files in os.walk(folder_path):  # os.walk traverses all subfolders and files.
        for file in files:
            file_path = os.path.join(root, file)  # Combines the folder path and file name.
            extension = get_file_extension(file_path)  # Determines the file's type based on its extension.
            file_size = os.path.getsize(file_path)  # Retrieves the file's size in bytes.
            file_hash = calculate_file_hash(file_path)  # Generates a hash to detect duplicates.

            # Categorizes files by type, adding their sizes.
            if extension not in file_types:
                file_types[extension] = 0
            file_types[extension] += file_size

            # Checks for duplicate files based on their hash.
            if file_hash in duplicate_files:
                duplicate_files[file_hash].append(file_path)  # Adds the file to the existing duplicates list.
            else:
                duplicate_files[file_hash] = [file_path]  # Creates a new list for this file hash.

            # Records the file's size to identify the largest files later.
            file_sizes.append((file_path, file_size))

    # Sorts files by size in descending order and selects the top 5 largest.
    largest_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)[:5]

    # Filters out unique files, keeping only duplicates.
    duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}

    return file_types, duplicate_files, largest_files

def display_results(file_types, duplicate_files, largest_files):
    """
    Displays the results of the analysis:
    - How much space each file type uses.
    - Which files are duplicates.
    - The 5 largest files in the folder.
    """
    print("\n--- File Types and Storage Usage ---")
    for extension, size in file_types.items():
        print(f"{extension if extension else 'No Extension'}: {size / (1024 ** 2):.2f} MB")  # Converts bytes to MB for easier reading.

    print("\n--- Duplicate Files ---")
    if duplicate_files:
        for file_hash, files in duplicate_files.items():
            print(f"\nHash: {file_hash}")  # Shows the unique hash for the duplicate files.
            for file in files:
                print(f"  {file}")  # Lists all the files with the same content.
    else:
        print("No duplicate files found.")  # Indicates if no duplicates are present.

    print("\n--- Top 5 Largest Files ---")
    for file, size in largest_files:
        print(f"{file}: {size / (1024 ** 2):.2f} MB")  # Displays the file name and its size in MB.

if __name__ == "__main__":
    folder = input("Enter the folder path to analyze: ").strip()  # Prompts the user for the folder path.
    if os.path.exists(folder) and os.path.isdir(folder):  # Checks if the folder path exists and is valid.
        file_types, duplicate_files, largest_files = analyze_storage(folder)  # Runs the storage analysis.
        display_results(file_types, duplicate_files, largest_files)  # Outputs the results to the user.
    else:
        print("Invalid folder path. Please try again.")  # Shows an error if the folder path is invalid.


''' Example Output:

Enter the folder path to analyze: ./saquib_folder

--- File Types and Storage Usage ---
.txt: 6.00 MB
.jpg: 5.00 MB
.mp4: 50.00 MB
.png: 10.00 MB
.docx: 3.00 MB

--- Duplicate Files ---
Hash: a1b2c3d4e5f67890abcd1234567890abcdef1234567890abcd1234567890abc
  ./saquib_folder/duplicate_file.jpg
  ./saquib_folder/duplicate_file_copy.jpg

--- Top 5 Largest Files ---
./saquib_folder/video.mp4: 50.00 MB
./saquib_folder/image.png: 10.00 MB
./saquib_folder/file1.txt: 3.00 MB
./saquib_folder/file2.txt: 3.00 MB
./saquib_folder/docs/report.docx: 2.00 MB
'''