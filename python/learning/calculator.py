num1 = float(input("Enter first value: "))
symbol = input("Enter operater (+,-,*,/): ")
num2 = float(input("Enter second value: "))

if symbol == "+" :
    result = (num1 + num2)
    print(round(result , 4))
elif symbol == "-" :
    result = (num1 - num2)
    print(round(result , 4))
elif symbol == "*" :
    result = (num1 * num2)
    print(round(result , 4))
elif symbol == "/": 
    result = (num1 / num2)
    print(round(result , 4))
else :  print(f"{symbol} is an invalid operator , try again.")