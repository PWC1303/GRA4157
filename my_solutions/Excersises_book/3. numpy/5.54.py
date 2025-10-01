import numpy as np
import random

def test_addition():
    n= 4
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    result1 = A+B
    result2= B+A
    tol = 1e-14


    if  abs (result1-result2).max() < tol:
        print("verified")

    else: 
        print("nah")

    

def test_commutivity():
    n= 4
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    C = np.random.rand(n,n)
    result1 = np.matmul((A+B),C)
    result2= np.matmul(A,C)+np.matmul(B,C)
    tol = 1e-14


    if  abs (result1-result2).max() < tol:
        print("verified")

    else: 
        print("nah")
test_addition()
test_commutivity()
