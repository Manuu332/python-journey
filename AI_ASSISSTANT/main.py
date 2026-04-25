from notes import (
    add_note, 
    list_notes, 
    delete_note, 
    search_notes, 
    recent_notes, 
    count_notes, 
    )

def show_help():
    print("\nCommands: ")
    print("remember <text> - Save something to memory")
    print("add <text>      - Add a new note")
    print("show notes      - Show all notes")
    print("list            - Show all notes")
    print("recent          - Show most recent notes")
    print("count           - Show total number of notes")
    print("delete <number> - Delete a note by number")
    print("search <word>   - Search notes by keyword")
    print("help            - Show this help message")
    print("exit            - Quit the program\n")

show_help()

while True:
    command = input("You: ").strip()

    if command in ("add", "remember"):
        add_note("")
    
    elif command.startswith("add "):
        text = command[4:]
        add_note(text)
    
    elif command.startswith("remember: "):
        text = command[9:]
        add_note(text)

    elif command in ("list", "show notes"):
        list_notes()
    
    elif command == "recent":
        recent_notes()

    elif command == "count":
        count_notes()

    elif command == "delete":
        print("Enter note number to delete")

    elif command.startswith("delete "):
        number_text = command[7:].strip()

        if not number_text.isdigit():
            print("Please enter a valid note number.")
            continue

        delete_note(int(number_text))

    elif command == "search":
        search_notes("")

    elif command.startswith("search "):
        keyword = command[7:]
        search_notes(keyword)

    elif command == "help":
        show_help()
    
    elif command == "exit":
        print("Later, then 🤗.")
        break
    
    else:
        print("I didn't get that. Type 'help' to see available commands.")