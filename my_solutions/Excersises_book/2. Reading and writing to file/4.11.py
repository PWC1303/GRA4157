import sys 




try:
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])

    g = 9.81 

    y = v0*t-0.5*g*t**2 
except (ValueError,TypeError):
    print("please give a float for t and float for v0 also make sure to have spacing in between")
except IndexError:
    print("well well well make sure to give to arguments idiot fucking reatard")