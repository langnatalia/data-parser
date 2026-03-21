# utils.py

import os
import re
import json
from datetime import datetime

def load_json(file_path):
    """Loads a JSON file and returns its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    """Saves the given data into a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def extract_date(text):
    """Extracts a date from a string."""
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    match = re.search(date_pattern, text)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d')
    return None

def get_file_extension(file_path):
    """Gets the file extension from a file path."""
    return os.path.splitext(file_path)[1]