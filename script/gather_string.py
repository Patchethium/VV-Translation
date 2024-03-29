import os
import re
import json

def extract_japanese_text(file_path):
    japanese_texts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            # Check if line contains comments, if so, remove them
            line = re.sub(r'//.*|<!--.*?-->', '', line)
            # Extract Japanese text from the line
            japanese_matches = re.findall(r'[\u3040-\u30FF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+', line)
            if japanese_matches:
                japanese_text = " ".join(japanese_matches)
                # Extracting neighbor lines with indent
                neighbors = []
                start_line = max(1, line_number - 5)
                end_line = min(len(lines), line_number + 6)
                for i in range(start_line, end_line):
                    indent = len(lines[i-1]) - len(lines[i-1].lstrip())
                    spaces = ' ' * indent
                    neighbors.append(f"{spaces}{lines[i-1].strip()}")
                japanese_texts.append({'neighbors': neighbors, 'text': japanese_text, 'translation': ''})
    return japanese_texts

def process_directory(directory):
    japanese_texts = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.vue', '.ts')):
                file_path = os.path.join(root, file)
                japanese_lines = extract_japanese_text(file_path)
                if japanese_lines:
                    japanese_texts[file] = japanese_lines
    return japanese_texts

def main():
    directory = input("Enter the directory path: ")
    japanese_texts = process_directory(directory)
    with open("strings.json", 'w', encoding='utf-8') as json_file:
        json.dump(japanese_texts, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
