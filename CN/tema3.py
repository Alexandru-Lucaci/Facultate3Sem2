import subprocess
import sys
from threading import Thread
import time
try:
    import numpy as np
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
try:
    import matplotlib.pyplot as plt
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

def log(type, message,error = False):
    if error == True:
        print("[" + type + "] "+" [ERRO] " + message)
    else:   
        print("[" + type + "] " + message)
        
def createInMatrix(n):
    return np.identity(n)

def HouseholderAlg(A,b):
    # u vector
    u=np.zeros(A.shape[0])
    epsilon = 0.0000001
    n=A.shape[0]
    Qbarat = createInMatrix(A.shape[0])
    print("Qbarat", Qbarat)
    # A = QR
    for r in range(n-1):
        # u=np.zeros(A.shape[0])
        # cosntruct Pr - projection matrix 
        # sigma = sign(a[r+1][r]) * ||a[r+1][r]||_2
        sigma = 0
        for i in range(r, n):
            sigma += A[i][r]**2
        if sigma < epsilon:
            # r=r+1 if and only if Pr = In
            break
        k = sigma**0.5
        if A[r][r] >0:
            k = -k
        beta = sigma - k*A[r][r]

        # construct Pr
        u[r] = A[r][r] - k
        for i in range(r+1, n):
            u[i] = A[i][r]
        
        # A = Pr*A
        # transformarea coloanelor j = r+1,...,n-1
        for j in range (r+1,n):
            # y = yi/beta = (Aej,u)/beta = sum from i=r to n-1 of Aij*ui/beta)
            y = 0
            for i in range(r, n):
                y += A[i][j]*u[i]/beta
            # Aij = Aij - yui
            for i in range(r, n):
                A[i][j] -= y*u[i]
            
        # transformarea coloanei r a matricei A
        A[r][r] = k
        for i in range(r+1, n):
            A[i][r] = 0
        
        # b = Pr*b
        
        for i in range(r, n):
            u[i] = u[i]/beta
        for i in (r,n-1):
            b[i] = b[i] - u[i]*b[r]
        # Qbarat = Qbarat*Pr
        for j in range(n):
            
            for i in range(r, n):
                
                Qbarat[i][j] -= u[i]*Qbarat[r][j]
    return Qbarat,A

# test
A = np.array([[0,0,4],[1,2,3],[0,1,2]])
s = np.array([3,2,1])

print(HouseholderAlg(A,s))




#  exercitiul 1
# Se dau n dimensiunea sistemului, Epsilon eroarea, A matricea sistemului, s un vector
def get_b_vector(n,A,s):
    b = np.array([0]*n)
    for i in range(n):
        sum = 0 
        for j in range(n):
            sum += A[i][j]*s[j]
        b[i] = sum
    return b

# print(get_b_vector(3,A,s))
        