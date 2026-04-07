from notes import add_note , list_notes

while True:
    command = input(">>")

    if command.startswith("add"):
        text = command[4:]
        add_note(text)
    elif command == "list":
        list_notes()
    elif command == "exit":
        break