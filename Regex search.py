print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import os
import re

def search_regex_in_txt_files(folder_path, pattern):
    regex = re.compile(pattern)
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        for line_num, line in enumerate(file, 1):
                            if regex.search(line):
                                print(f"{filename} (line {line_num}): {line.strip()}")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
    except FileNotFoundError:
        print(f"Error: Folder not found at '{folder_path}'. Please enter a valid folder path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

folder = input("Enter the folder path: ")
pattern = input("Enter the regex pattern to search: ")

search_regex_in_txt_files(folder, pattern)
