import sys


arglist =[]

for argument in sys.argv[1:]:
    try:
        argument = int(argument)
        arglist.append(argument)
        print(f"number {argument} is int")
        continue
    except:
          print("Could not convert to int, we are trying float")
    try:
        argument = float(argument)
        arglist.append(argument)
        print(f"number {argument} is float")
    except: 
         print("Invalid input could not convert to float either,skipping this one")
         continue


if len(arglist) == 2: 
    number1 = arglist[0]
    number2 = arglist[1]
    if number1 or number2 == 0:
         print("division by zero not allowed")
    else:
        remainder = number1 % number2
        quotient= ((number1-remainder)/number2)
        print(f"For {number1} & {number2} the remainder is {remainder} and quotient is {quotient} ")

for number in arglist[1:]:
        if number == 0: 
            print("You can not divide by zero, skipping this number")
            continue
        if  number % 2 ==0:
            print(f"{number} is Even Steven")
        else:
            print(f"{number} is Odd Bob,")

 