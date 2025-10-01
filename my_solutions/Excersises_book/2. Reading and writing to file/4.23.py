import random
import sys


A = int(sys.argv[1])
B = int(sys.argv[2])
n = int(sys.argv[3])
def power3_identity(A,B,n):
    counter = 0
    for _ in range(n):
        a = random.uniform(A,B)
        b = random.uniform(A,B)

        if (a*b)**3 != (a**3)*(b**3):
            counter =counter + 1 
    failures = counter/n

    return failures
failures = power3_identity(A,B,n)
print(f"Fraction of failures where {failures}")




