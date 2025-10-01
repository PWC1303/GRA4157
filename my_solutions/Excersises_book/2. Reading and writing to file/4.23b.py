import random
import sys


A = int(sys.argv[1])
B = int(sys.argv[2])
n = int(sys.argv[3])
expr1 = sys.argv[4]
expr2 = sys.argv[5]




def power3_identity(expr1, expr2, A,B,n):
    counter = 0
    
    for _ in range(n):
        a = random.uniform(A,B)
        b = random.uniform(A,B)
        val1 = eval(expr1)
        val2 = eval(expr2)
        print(val1)

        if val1!= val2:
            counter =counter + 1 
    failures = counter/n

    return failures
failures = power3_identity(expr1, expr2, A,B,n)
print(f"Fraction of failures where {failures}")

