questions = ("Which character in Saiki K claims to have powers he must seal in his arm?", 
             "In Hell's Paradise, what is the main chaacter's title?", 
             "What are the the highest ranking demons in Demon Slayer called?", 
             "How many titan-shifting abilities did Eren have at the end of season 4?", 
             "In Dragon Balls, what is used to restore a Z fighter's health after exhaustion or being wounded?", 
             "What is the greatest taboo among alchemists in Fullmetal Alchemist?", 
             )

options = (("A. Nendou", "B. Kaidou", "C. Teruhashi", "D. Kobuyasu"),
           ("A. Gabimaru The Ugly", "B. Gabimaru The Immortal", "C. Gabimaru The Ruthless", "D. Gabimaru The Hollow"),
           ("A. Mizunoto", "B. Hashira", "C. Kizuki", "D. Kakushi"),
           ("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. Green Tea", "B. Ramen", "C. Rumble Ball", "D. Senzu Bean"),
           ("A. Human transfiguration", "B. Human transeference", "C. Human transmutation", "D. Gold transmutation"))

answers = ("B", "D", "C", "B", "D", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("YOU'RE RIGHT!")
    else:
        print("NOPE!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("Your guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")

print()

print("The answers: ", end = "")
for answer in answers:
    print(answer, end = " ")

print()

score = int(score / len(questions) * 100)
print (f"You got: {score}%")    