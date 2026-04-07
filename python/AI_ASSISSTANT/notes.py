from storage import load_notes , save_notes

def add_note(text):
    notes = load_notes()
    notes.append(text)
    save_notes(notes)
    print("Note added.")

def list_notes():
    notes = load_notes()

    for i, note in enumerate(notes):
        print(f"{i + 1}.{note}")