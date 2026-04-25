username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't be more than 12 letters")
elif not username.find(" ") == -1:
    print("Username can't have spaces")
elif not username.isalpha():
    print("Username can't contain a number")
else:
    print(f"Hey {username}. How nice of you to visit us again.")