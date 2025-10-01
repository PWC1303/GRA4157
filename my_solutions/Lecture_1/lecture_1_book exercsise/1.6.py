import sys 
argument = input("provide deposit, interest and years in this format, deposit, interest,years")

argument = argument.split(",")

A = float(argument[0])
p = float(argument[1])
n = float(argument[2])


def annual_compunding(A,p,n):
 
    FV = A*(1 +p)**n
    return FV

print(annual_compunding(A,p,n))