print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import os
import shutil

source_folder = input("Enter the folder to search in: ")
destination_folder = input("Enter the destination folder: ")
extension = input("Enter the file extension (e.g., .jpg, .pdf): ").lower()

os.makedirs(destination_folder, exist_ok=True)

file_count = 0
for foldername, subfolders, filenames in os.walk(source_folder):
    for filename in filenames:
        if filename.lower().endswith(extension):
            source_path = os.path.join(foldername, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.copy2(source_path, destination_path)
            file_count += 1
            print(f"Copied: {filename}")

print(f"\nDone! {file_count} '{extension}' file(s) copied to '{destination_folder}'.")
