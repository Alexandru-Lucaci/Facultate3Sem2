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
try:
    import scipy
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
def log(type, message,error = False):
    if error == True:
        print("[" + type + "] "+" [ERRO] " + message)
    else:   
        print("[" + type + "] " + message)
        
def createInMatrix(n):
    return np.identity(n)

def transpusa(A):
    return np.transpose(A)

def HouseholderAlg(A,b):
    # u vector
    u=np.zeros(A.shape[0])
    epsilon = 0.00001
    n=A.shape[0]
    Qbarat = createInMatrix(A.shape[0])
    # A = QR
    for r in range(n-1):
        # print("r=",r)
        # u=np.zeros(A.shape[0])
        # cosntruct Pr - projection matrix 
        # sigma = sign(a[r+1][r]) * ||a[r+1][r]||_2
        sigma = 0
        for i in range(r, n):
            # print(f"A[{i}][{r}]={A[i][r]}")
            sigma += A[i][r]**2
        if sigma < epsilon:
            # r=r+1 if and only if Pr = In
            print('break')
            break
        # print("sigma=",sigma)
        k = sigma**0.5
        # print("k=",k)
        if A[r][r] >0:
            k = -k
        beta = sigma - k*A[r][r]
        # print("beta=",beta)
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
                y += A[i][j]*u[i]
            y = y/beta
            # Aij = Aij - yui
            for i in range(r, n):
                A[i][j] -= y*u[i]
            
        # transformarea coloanei r a matricei A
        A[r][r] = k
        for i in range(r+1, n):
            A[i][r] = 0
        
        # b = Pr*b
        # print("b before", b)
        y= 0
        for i in range(r, n):
            y+= b[i]*u[i]
        y = y/beta
        for i in range(r, n):
            b[i] -= y*u[i]        
        # print("b after", b)


        # Qbarat = Qbarat*Pr
        # transformarea coloanelor j = r+1,...,n-1
        # print("Qbarat before", Qbarat)
        for j in range(n):
            y=0
            for i in range(r, n):
                y += Qbarat[i][j]*u[i]
            y = y/beta
            for i in range(r, n):
                Qbarat[i][j] -= u[i]*y
            
        # print("R", transpusa(Qbarat))
        # print("Q", A)
    return transpusa(Qbarat),A

# test
A = np.array([[0,0,4],[1,2,3],[0,1,2]])
s = np.array([4,10,4])
# print(transpusa(A))
# q,r = HouseholderAlg(A,s)
# q,r=HouseholderAlg(A,s)

# print("Q", q,'\n')
# print("R", r,'\n')
# # multiplication q r
# print("q r", np.matmul(q,r))



#  exercitiul 1
# Se dau n dimensiunea sistemului, Epsilon eroarea, A matricea sistemului, s un vector
def get_b_vector(n,A,s):
    b = np.array([0]*n)
    for i in range(n):
        sum = 0 
        for j in range(n):
            sum += A[i][j]*s[j]
        b[i] = sum
    reversedX = np.array([0]*n)
    for i in range(n):
        reversedX[i] = b[n-i-1]
    return reversedX

# print(get_b_vector(3,A,s))

def doMultimplication(A,b):
    n = len(b)
    x = np.array([0]*n)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i][j]*b[j]
        x[i] = sum
        
    #  reverse x
    reversedX = np.array([0]*n)
    for i in range(n):
        reversedX[i] = x[n-i-1]
    return reversedX

def printSystem(A,b):
    # print x1 + x2 + x3 = 3
    #       x1 + 2x2 + 3x3 = 2
    for i in range(A.shape[0]):
        if(i == 0):
            print("Sistemul este: \n\t",end='')
        for j in range(A.shape[1]):
            if A[i,j] !=0:
                if j == A.shape[1]-1:
                    if A[i,j] == 1:
                        print(f"x{j+1}", end='')  
                    else:
                            print(f"{A[i,j]}*x{j+1}", end='')
                else:
                    if A[i,j] == 1:
                        print(f"x{j+1}+", end='')  
                    else:
                        print(f"{A[i,j]}*x{j+1}+", end='')
        if i == A.shape[0]-1:
            print(f" = {b[i]}")
        else:                
            print(f" = {b[i]}\n\t",end='')


def resolveLiniarSystem(A,b,sciHub = False):
    n= A.shape[0]
    x = np.array([0]*n)
    # printSystem(A,b)
    if sciHub:
        q, r = scipy.linalg.qr(A)
    else:
        q,r = HouseholderAlg(A,b)
        #  rezolvam sistemul R*x = Q^T*b
    q = transpusa(q)
    # for my algorithm
    QtB = doMultimplication(q,b)
    # for sciHub
    if sciHub:
        QtB = np.matmul(q,b)
    # print(r,QtB)
    # rezolvam sistemul R*x = QtB
    printSystem(r,QtB)
 
    for i in range(n,0,-1):
        sum = 0
        for j in range(i,n):
            sum += r[i-1][j]*x[j]
        x[i-1] = (QtB[i-1] - sum)/r[i-1][i-1]

    print("Solutia este: ",x)
    

    
resolveLiniarSystem(A,s,True)
resolveLiniarSystem(A,s,False)