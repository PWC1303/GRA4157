import sys 


status = 1

while status == 1:

    try:
        #t = float(sys.argv[1])
        #v0 = float(sys.argv[2])

        t = float(input("enter t"))
        v0 = float(input("enter v0"))
        g = 9.81 


        cons_upper = 2*(v0/g) 
        cons_lower = 0 

        if not (0<= t <= cons_upper):
            raise ArithmeticError("Constraint violated")

        else:
            
            y = v0*t-0.5*g*t**2 
            print(y)
            status = 0
            
    except (ValueError,TypeError):
        print("please give a float for t and float for v0 also make sure to have spacing in between")
    except IndexError:
        print("well well well make sure to give to arguments idiot fucking reatard")
    except ArithmeticError as e:
        print(e)