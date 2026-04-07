#compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("How much is the principal: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("What is the rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = float(input("How long is the period (years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = principal * pow((1 + rate/100), time)

print (f"Well, your interest after {time} year/s will be Ksh{total:.2f}")


#==========OR==========#


principal = 0
rate = 0
time = 0

while True:
    principal = float(input("How much is the principal: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("What is the rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")
    else:
        break    

while True:
    time = float(input("How long is the period (years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principal * pow((1 + rate/100), time)

print (f"Well, your interest after {time} year/s will be Ksh{total:.2f}")