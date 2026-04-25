from storage import load_notes , save_notes

def add_note(text):
    text = text.strip()

    if not text:
        print("What would you like me to remember?")
        return
    
    notes = load_notes()
    notes.append(text)
    save_notes(notes)
    print("Noted 👍.")

def list_notes():
    notes = load_notes()

    if not notes:
        print("Nothing here yet.")
        return

    print("Here's what I got:")
    for i, note in enumerate(notes , start = 1):
        print(f"{i}. {note}")

def delete_note(note_number):
    notes = load_notes()

    if not notes:
        print("There's nothing to delete 🤷‍♂️.")
        return
    
    if note_number < 1 or note_number > len(notes):
        print("That note number is bogus.")
        return

    removed_note = notes.pop(note_number - 1)
    save_notes(notes)
    print(f"{removed_note} has been successfully deleted.")

def search_notes(keyword):
    keyword = keyword.strip()

    if not keyword:
        print("What are you searching for?")
        return

    notes = load_notes()
    matches = []

    for i , note in enumerate(notes , start = 1):
        if keyword.lower() in note.lower():
            matches.append((i , note))

    if not matches:
        print("I couldn't find a match 🤷‍♂️.")
        return
        
    print("This is what I got:")
    for number , note in matches:
        print(f"{number}. {note}")

def recent_notes(limit = 3):
    notes = load_notes()

    if not notes:
        print("Nothing here yet.")
        return
    
    print("Here are your most recent notes:")
    start = max(0 , len(notes) - limit)
    for i in range(len(notes) - 1 , start -1 , -1):
        print(f"{i + 1}. {notes[i]}")

def count_notes():
    notes = load_notes()
    print(f"You have {len(notes)} note(s) saved.")