email = input("What's your email ?")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and the domain is {domain}.")
#........OR.........

email = input ("What's your email ?")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and your domain is {domain}.")