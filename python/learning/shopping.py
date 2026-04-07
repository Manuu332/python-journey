#shopping list program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (Press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: Ksh "))
        foods.append(food)
        prices.append(price)

print("=======YOUR LIST=======")

for food in foods:
    print(food) # OR print(food, end=" ") *for a horizontal list (space btwn apostrophes = space between items)

for price in prices:
    total += price #OR total = total + price

print() # for an empty line
print(f"Your total is Ksh {total}")