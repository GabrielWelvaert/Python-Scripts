import os

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return sum(1 for _ in file)

def count_lines_in_directory(directory='.'):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                total_lines += count_lines_in_file(file_path)
                print(f"Counted lines in: {file_path}")
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    return total_lines

if __name__ == "__main__":
    total_lines = count_lines_in_directory()
    print(f"Total number of lines in all files: {total_lines}")
