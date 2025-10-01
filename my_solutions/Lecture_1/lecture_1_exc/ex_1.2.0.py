import sys

#try:
arglist = sys.argv



for number in arglist[1:]:
        
        try:
            number = float(number)
        except ValueError:
            print("Invalid input, please enter a number, skipping this one")
            continue
        if number == 0: 
            print("You can not divide by zero, skipping this number")
            continue
    
        if number % 2 ==0:
        
            print("Even Steven")
        else:
            print("Odd Bob")

    
#except ValueError:
 #    print("Invalid input. Please enter a number.")
#except IndexError:
 #    print("No input detected")


