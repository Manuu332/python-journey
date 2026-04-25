import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FILE_PATH = DATA_DIR / "notes.json"

def load_notes():
    if not FILE_PATH.exists():
        return[]
    
    try:
        with open(FILE_PATH , "r" , encoding = "utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]
    
def save_notes(notes):
    DATA_DIR.mkdir(exist_ok = True)
    
    with open(FILE_PATH , "w" , encoding = "utf-8") as file:
        json.dump(notes , file , indent = 2) 