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
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "matplotlib"])


def log(type, message, error=False):
    if error == True:
        print("[" + type + "] "+" [ERRO] " + message)
    else:
        print("[" + type + "] " + message)


def clasic_add(a, b):
    # Verificăm dacă matricele sunt de dimensiuni adecvate pentru a fi înmulțite
    if a.shape[0] != b.shape[0]:
        log("ADD", "Matricele nu au aceeasi dimensiune", True)
        return None
    else:
        c = np.zeros((a.shape[0], a.shape[1]))
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                c[i][j] = a[i][j] + b[i][j]
        return c


def clasic_sub(a, b):
    # Verificăm dacă matricele sunt de dimensiuni adecvate pentru a fi înmulțite

    if a.shape[0] != b.shape[0]:
        log("SUB", "Matricele nu au aceeasi dimensiune", True)
        return None
    else:
        c = np.zeros((a.shape[0], a.shape[1]))
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                c[i][j] = a[i][j] - b[i][j]
        return c


def strassen_algorithm(a, b):
    """
    Funcția care implementează algoritmul lui Strassen de înmulțire a matricelor
    """
    # Verificăm dacă matricele sunt de dimensiuni adecvate pentru a fi înmulțite

    # assert a.shape[0] == b.shape[0]
    # assert len(a.shape) == 2
    # assert a.shape[0] == a.shape[1] == b.shape[0] == b.shape[1]

    # Verificăm dacă matricele sunt de dimensiune 1, caz în care nu mai putem să le împărțim
    if a.shape[0] == 1:
        return a * b
    # calculate for 2x2
    if a.shape[0] == 2:
        c = np.zeros((2, 2))
        c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return c
    # Împărțim matricele în submatrice
    n = a.shape[0]
    m = n // 2

    a11 = a[:m, :m]
    a12 = a[:m, m:]
    a21 = a[m:, :m]
    a22 = a[m:, m:]

    b11 = b[:m, :m]
    b12 = b[:m, m:]
    b21 = b[m:, :m]
    b22 = b[m:, m:]

    # Aplicăm recursiv algoritmul lui Strassen pentru a calcula produsele matricei
    p1 = strassen_algorithm(clasic_add(a11, a22), clasic_add(b11, b22))
    p2 = strassen_algorithm(clasic_add(a21, a22), b11)
    p3 = strassen_algorithm(a11, clasic_sub(b12, b22))
    p4 = strassen_algorithm(a22, clasic_sub(b21, b11))
    p5 = strassen_algorithm(clasic_add(a11, a12), b22)
    p6 = strassen_algorithm(clasic_sub(a21, a11), clasic_add(b11, b12))
    p7 = strassen_algorithm(clasic_sub(a12, a22), clasic_add(b21, b22))

    c11 = clasic_add(clasic_sub(clasic_add(p1, p4), p5), p7)
    c12 = clasic_add(p3, p5)
    c21 = clasic_add(p2, p4)
    c22 = clasic_add(clasic_add(clasic_sub(p1, p2), p3), p6)
    # Construim matricea C din submatricile calculare anterior

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    # vstack - vertical stack - concateneaza matricile pe verticala
    # hstack - horizontal stack - concateneaza matricile pe orizontala
    return c


def generate_matrix(n):
    print("Generez o matrice de dimensiune: ", n)
    a = np.random.randint(1, 5, (n, n))
    print(a)
    return a


def np_multiplication(a, b):
    return np.matmul(a, b)


def clasic_multiplication(a, b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                a[i][j] += a[i][k] * b[k][j]


def funct_mul_np(a, b, result):
    start = time.time()
    result[0] = np.matmul(a, b)
    end = time.time()
    result[1] = end - start


def funct_mul_strassen(a, b, result):
    start = time.time()
    result[0] = strassen_algorithm(a, b)
    end = time.time()
    result[1] = end - start


def funct_mul_clasic(a, b, result):
    start = time.time()
    clasic_multiplication(a, b)
    end = time.time()
    result[1] = end - start


def create_graph_with_time():
    n = 32
    n_max = 1024
    n_min = 1
    step = 2
    x = []
    y1 = []
    y2 = []
    y3 = []

    while n <= n_max:
        x.append(n)
        a = generate_matrix(n)
        b = generate_matrix(n)
        # start = time.time()
        # clasic_multiplication(a, b)
        # end = time.time()
        result1 = [None]*2
        thread1 = Thread(target=funct_mul_np, args=(a, b, result1))
        thread1.start()
        result2 = [None]*2
        thread2 = Thread(target=funct_mul_strassen, args=(a, b, result2))
        thread2.start()
        result3 = [None]*2
        thread3 = Thread(target=funct_mul_clasic, args=(a, b, result3))
        thread3.start()
        thread1.join()
        thread2.join()
        thread3.join()
        y1.append(result1[1])
        # start = time.time()
        # np_multiplication(a, b)
        # end = time.time()
        y2.append(result2[1])
        # start = time.time()
        # strassen_algorithm(a, b)
        # end = time.time()
        y3.append(result3[1])
        n *= step

    plt.plot(x, y1, label="Multiplication clasic")
    plt.plot(x, y2, label="Multiplication numpy")
    plt.plot(x, y3, label="Multiplication strassen")
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.legend()
    plt.show()


# example
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
c = strassen_algorithm(a, b)

print(np.matmul(a, b))
print(c)
