print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import os

def find_large_files(folder, size_limit_mb=100):
    size_limit_bytes = size_limit_mb * 1024 * 1024  

    print(f"\nFiles larger than {size_limit_mb}MB in '{folder}':\n")

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_limit_bytes:
                    size_in_mb = file_size / (1024 * 1024)
                    print(f"{os.path.abspath(file_path)} - {size_in_mb:.2f} MB")
            except Exception as e:
                print(f"Could not access {file_path}: {e}")


target_folder = input("Enter the folder path to scan: ")
find_large_files(target_folder)
