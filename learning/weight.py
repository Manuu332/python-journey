#weight converter

weight = float(input("Eka weight, don't be shy: "))
unitx = input("Enter the unit of weight (kg, g, t, mg): ")
unity = input("Enter the unit to convert to (kg, g, t, mg): ")

if unitx == "kg" and unity == "g" :
    result = weight * 1000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "kg" and unity == "t" :
    result = weight / 1000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
elif unitx == "kg" and unity == "mg" :
    result = weight * 1000000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "g" and unity == "kg" :
    result = weight / 1000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
elif unitx == "g" and unity == "t" :
    result = weight / 1000000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
elif unitx == "g" and unity == "mg" :
    result = weight * 1000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "t" and unity == "kg" :
    result = weight * 1000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "t" and unity == "g" :
    result = weight * 1000000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "t" and unity == "mg" :
    result = weight * 1000000000
    print(f"{weight} {unitx} is equal to {result} {unity}")
elif unitx == "mg" and unity == "kg" :
    result = weight / 1000000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
elif unitx == "mg" and unity == "g" :
    result = weight / 1000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
elif unitx == "mg" and unity == "t" :
    result = weight / 1000000000
    print(f"{weight} {unitx} is equal to {round(result, 4)} {unity}")
else : print(f"{unitx} or {unity} is an invalid unit , try again.")