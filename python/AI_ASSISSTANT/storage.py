import json

FILE_PATH = "data/notes.json"

def load_notes():
    with open(FILE_PATH , "r") as f:
        return json.load(f)
    
def save_notes(notes):
    with open(FILE_PATH , "w") as f:
        json.dump(notes , f , indent = 2)  