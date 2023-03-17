import subprocess
import sys
from threading import Thread
import time
import math
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
A = np.array([[0,0,4],[1,2,3],[0,1,2]], dtype='f')
s = np.array([4,10,4], dtype='f')
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
    b = np.array([0]*n, dtype='f')
    for i in range(n):
        sum = 0 
        for j in range(n):
            sum += A[i][j]*s[j]
        b[i] = sum
    reversedX = np.array([0]*n, dtype='f')
    for i in range(n):
        reversedX[i] = b[n-i-1]
    return reversedX

# print(get_b_vector(3,A,s))

def doMultimplication(A,b):
    n = len(b)
    x = np.array([0]*n, dtype='f')
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i][j]*b[j]
        x[i] = sum
        
    #  reverse x
    reversedX = np.array([0]*n, dtype='f')
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
    x = np.array([0]*n, dtype='f')
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
    return x

    
# resolveLiniarSystem(A,s,True)
# resolveLiniarSystem(A,s,False)
def calcul_norma(A,b):
    resolverMy = resolveLiniarSystem(A,b,False)
    resolverScipY = resolveLiniarSystem(A,b,True)
    # calcul norma
    norma = 0
    for i in range(len(b)):
        norma += (resolverMy[i] - resolverScipY[i])**2
    return math.sqrt(norma)

# print( calcul_norma(A,s))

def subVect(x,y):
    n = len(x)
    z = np.array([0]*n, dtype='f')
    print(x,y)
    for i in range(n):
        z[i] = (x[i]**2) - (y[i]**2)
    return z
def calcul_norma2(A,b):
    print("A",A)
    print("b",b)
    myResolve = resolveLiniarSystem(A,b,False)
    print("myResolve",myResolve)
    multiplication = doMultimplication(A,myResolve)
    print("multiplication",multiplication)
    sub = subVect(multiplication,b)
    print("sub",sub)
    #  calcul norma
    norma = 0
    for i in range(len(b)):
        norma += (sub[i])
    return math.sqrt(norma)


print(calcul_norma2(A,s))
def calcul_norma3(A,b):
    print("A",A)
    print("b",b)
    myResolve = resolveLiniarSystem(A,b,True)
    print("myResolve",myResolve)
    multiplication = doMultimplication(A,myResolve)
    print("multiplication",multiplication)
    sub = subVect(multiplication,b)
    print("sub",sub)
    #  calcul norma
    norma = 0
    for i in range(len(b)):
        norma += (sub[i])
    return math.sqrt(norma)
A = np.array([[0,0,4],[1,2,3],[0,1,2]], dtype='f')
s = np.array([4,10,4], dtype='f')
print(calcul_norma3(A,s))


def calcul_norma4(A,b):
    myResolve = resolveLiniarSystem(A,b)
    suma = 0 
    for i in range(len(b)):
        suma += ((myResolve[i]) - (b[i]))**2
    print(suma)
    norma = math.sqrt(suma)
    suma = 0 
    for i in range(len(b)):
        suma += b[i]**2
    print (suma)
    norma = norma/math.sqrt(suma)
    return norma
print(calcul_norma4(A,s))

def calcDeterminant(A):
    n = A.shape[0]
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det
def generate_epsilon(m):
    epsilon = 1
    for i in range(m):
        epsilon /= 10
    return epsilon
def inverse_qr(A):
    epsilon = generate_epsilon(6)
    Q, R = HouseholderAlg(A,[0]*A.shape[0])
    n = A.shape[0]
    A_inv = [[0.0]*n for i in range(n)]
    if calcDeterminant(R) < epsilon:
        return False
    else:
        for j in range(n):
            ej = np.array([0]*n, dtype='f')
            ej[j] = 1
            QT = transpusa(Q)
            b = doMultimplication(QT,ej)
            print(f'{j} {b}')
            # RX = b
            # reverse b
            reversed_b = np.array([0]*n, dtype='f')
            for i in range(n):
                reversed_b[i] = b[n-i-1]
            b= reversed_b
            x = [0.0]*n
            printSystem(R,b)
            for i in range(n,0,-1):
                sum = 0
                for lj in range(i,n):
                    sum += R[i-1][lj]*x[lj]
                print(f"(b[i-1] - sum) = {b[i-1]} - {sum} = {b[i-1] - sum}")
                print(f"R[i-1][i-1] = {R[i-1][i-1]}")
                print (f"(b[i-1] - sum)/R[i-1][i-1]) = {(b[i-1] - sum)/R[i-1][i-1]}")
                x[i-1] = float((b[i-1] - sum)/R[i-1][i-1])
            # add x to column j of A_inv
            print(j,x)
            for k in range(n):
                A_inv[j][k] = x[k]
            print('done',A_inv)
        # print(A_inv)
        return A_inv
A = np.array([[0,0,4],[1,2,3],[0,1,2]])
s = np.array([4,10,4])
print(inverse_qr(A))
A = np.array([[0,0,4],[1,2,3],[0,1,2]])
s = np.array([4,10,4])
def calc_norm_inv(A):
    resolverScipY = np.linalg.inv(A)
    resolverMy = inverse_qr(A)
    print(resolverMy)
    print(resolverScipY)
   
    norma = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            norma += (resolverMy[i][j] - resolverScipY[j][i])**2
    return math.sqrt(norma)
import random
print(calc_norm_inv(A))
def generateRandomMatrixAndB(n):
    A = np.array([[0.0]*n for i in range(n)], dtype='f')
    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(1,10)
    b = [0]*n
    for i in range(n):
        b[i] = random.randint(1,10)
    return A, b
a,b = generateRandomMatrixAndB(3)

print(calcul_norma(a,b))