file_paths = ["boot.log"]



for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        line_count = sum(1 for _ in file)
        print(f"Total number of lines in {file_path} : {line_count}")
