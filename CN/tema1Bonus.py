import subprocess
import sys


def log(message: str, place: str, warning: bool = False, error: bool = False) -> str:
    """
    Print a message in the console with a specific format.

    Args:
        message (str): the string to be printed
        place (str): the place where the message is printed
        warning (bool, optional): Print [warning] in front of the text. Defaults to False.
        error (bool, optional): Print [Error] in front of the tex. Defaults to False.

    Returns:
        str: Final text with the format
    """
    if error:
        print(f"[Error][{place}]: {message}")

    else:
        if warning:
            print(f"[Warning][{place}]: {message}")
        else:
            print(f"[{place}]: {message}")


try:
    import numpy as np
except ImportError:
    log("Numpy is not installed", "Import", warning=True)
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])

try:
    import matplotlib.pyplot as plt
except ImportError:
    log("Matplotlib is not installed", "Import", warning=True)
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", 'matplotlib'])


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clasic_add(a, b):
    """Funcția adună două matrici de aceeași dimensiune"""
    # verifică dacă au aceeași dimensiune
    if a.shape[0] != b.shape[0]:
        log("ADD",
            f"Matricele nu au aceeasi dimensiune \n na.shape = {a.shape[0]} \n b.shape={b.shape[0]}", True)
        return None
    else:
        c = np.zeros((a.shape[0], a.shape[1]))
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                c[i][j] = a[i][j]+b[i][j]
        return c


n = 5
a = np.random.randint(1, 5, (n, n))
b = np.random.randint(1, 5, (n, n))


def clasic_sub(a, b):
    """Funcția scade două matrici de aceeași dimensiune"""
    # verifică dacă au aceeași dimensiune
    if a.shape[0] != b.shape[0]:
        log("SUB",
            f"Matricele nu au aceeasi dimensiune \n na.shape = {a.shape[0]} \n b.shape={b.shape[0]}", True)
        return None
    else:
        c = np.zeros((a.shape[0], a.shape[1]))
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                c[i][j] = a[i][j]-b[i][j]
        return c


def strassen_algorithm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Algoritmul lui Strassen pentru înmulțirea a două matrice

    Args:
    ----
        a (np.ndarray): Prima matrice
        b (np.ndarray): A doua matrice

    Returns:
    --------
        np.ndarray: Matricea rezultat
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


# example
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
c = strassen_algorithm(a, b)

print(np.matmul(a, b))
print(c)


# make a matrix square
def make_square_matrix(matrix: np.ndarray):
    """ Makes a matrix square by adding zeros to the rows or columns

    Args:
        matrix (np.ndarray): the matrix to be made square

    Returns:
        _type_: the square matrix
    """
    diference = matrix.shape[0] - matrix.shape[1]
    if diference > 0:
        # we need to add columns
        for i in range(diference):
            matrix = np.hstack((matrix, np.zeros((matrix.shape[0], 1))))
    else:
        # we need to add rows
        for i in range(-diference):
            matrix = np.vstack((matrix, np.zeros((1, matrix.shape[1]))))
    return matrix


# test make_square_matrix
print(make_square_matrix(
    np.array([[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [20, 21]])))


def generate_matrix(n):
    print("Generez o matrice de dimensiune: ", n)
    a = np.random.randint(1, 5, (n, n))
    print(a)
    return a
# print(make_square_matrix(generate_matrix(12)))
# make a squarte matrix with the lenght being a power of 2


def is_power_of_two(n: int) -> bool:
    """ Checks if a number is a power of 2

    Args:
        n (int): Number to be checked

    Returns:
        bool: True if the number is a power of 2, False otherwise
    """
    if n <= 0:
        return False
    return n & (n - 1) == 0


def make_same_nxn(a: np.ndarray, b: np.ndarray):
    """Resizes the matrices to be the same size by adding zeros to the rows and columns

    Args:
        a (np.ndarray): First matrix
        b (np.ndarray): First matrix

    Returns:
        _type_:  a and b resized to be the same size
    """
    if a.shape[0] == b.shape[0]:
        return (a, b)
    diference = a.shape[0] - b.shape[0]
    if diference > 0:
        # a has more rows and column
        for i in range(diference):
            b = np.vstack((b, np.zeros((1, b.shape[1]))))
            b = np.hstack((b, np.zeros((b.shape[0], 1))))
    else:
        # b has more rows and column
        for i in range(-diference):
            a = np.vstack((a, np.zeros((1, a.shape[1]))))
            a = np.hstack((a, np.zeros((a.shape[0], 1))))
    return (a, b)


def make_power2_matrix(matrix: np.ndarray) -> np.ndarray:
    """ Makes a matrix square and with the lenght being a power of 2

    Args:
        matrix (np.ndarray): Input matrix

    Returns:
        np.ndarray: The matrix made asqure and with the lenght being a power of 2
    """
    if matrix.shape[0] != matrix.shape[1]:
        log("make_square_matrix", "The matrix is not square", True)
        matrix = make_square_matrix(matrix)
    if matrix.shape[0] == 1:
        return matrix
    log(f"The matrix generated is{matrix} and its shape is {matrix.shape} ",
        "make_power2_matrix")
    iteration = 0
    while is_power_of_two(matrix.shape[0]) == False:
        iteration += 1
        log(f"{matrix.shape[0]**0.5 % 1}, {iteration}", "make_power2_matrix}")
        matrix = np.vstack((matrix, np.zeros((1, matrix.shape[1]))))
        matrix = np.hstack((matrix, np.zeros((matrix.shape[0], 1))))
    return matrix


# test make_power2_matrix
matrix = np.array([[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17]])
print(make_power2_matrix(matrix))


def try_reduce_matrix(matrix: np.ndarray):
    """Tries to reduce the matrix by removing the last row and column if they are all zeros

    Args:
    ----
        matrix (np.ndarray): The matrix to be reduced

    Returns:
    -------
        np.ndarray: The reduced matrix
    """
    if matrix.shape[0] == 1:
        return matrix
    # eliminate the last row
    while np.all(matrix[-1] == 0):
        matrix = matrix[:-1, :]
    # eliminate the last column
    while np.all(matrix[:, -1] == 0):
        matrix = matrix[:, :-1]

    return matrix


def strassen_alg_with_n(a, b):
    """Strassen algorithm with the matrices being of the diff size

    Args:
        a (_type_): First matrix
        b (_type_): Second matrix

    Returns:
        _type_: The product of the two matrices
    """
    a = make_power2_matrix(a)
    b = make_power2_matrix(b)
    a, b = make_same_nxn(a, b)
    log(f"Matricea a este \n{a}\n si are dimensiunea {a.shape}",
        "strassen_alg_with_n")
    log(f"Matricea b este \n{b}\n si are dimensiunea {b.shape}",
        "strassen_alg_with_n")
    return try_reduce_matrix(strassen_algorithm(a, b))


a = np.array([[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17]])
b = np.array([[1, 2], [4, 5]])
print(strassen_alg_with_n(a, b))
print(np.matmul(a, b))
