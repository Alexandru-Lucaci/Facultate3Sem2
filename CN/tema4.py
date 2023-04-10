
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
    import math
except ImportError:
    log("Math is not installed", "Import", warning=True)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "math"])
    import math
try:
    from tqdm import tqdm
except:
    log("Tqdm is not installed", "Import", warning=True)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm
try:
    import numpy as np
except ImportError:
    log("Numpy is not installed", "Import", warning=True)
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    import numpy as np
try:
    import matplotlib.pyplot as plt
except ImportError:
    log("Matplotlib is not installed", "Import", warning=True)
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", 'matplotlib'])
    import matplotlib.pyplot as plt
try:
    import scipy
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    import scipy


def definire_matrice_rara(file_name):
    """
It reads a file and returns a list of lists of tuples

Parameters:
-----------
:param file_name: the name of the file that contains the data

Returns:
--------
:return: A list of lists.
"""
    number_of_lines = 0  # number of lines in the file
    with open(file_name, "r") as f:
        # first line represents the number of lines in the file
        number_of_lines = int(f.readline())
        # print(number_of_lines)
        # create a list with the number of lines
        values = []
        # iterate throw all the lines
        # and append the values in the list
        # print(values)
        colsAndValues = ()

        for index, line in enumerate(f):
            line = line.strip().split(',')
            # colsAndValues = line.split(',')
            try:
                colsAndValues = (float(line[0]), int(line[2]))
            except:
                log("Error while converting to float",
                    "definire_matrice_rara", error=True)
                log(line, f"{index}", error=True)

            try:
                values[int(line[1])].append(colsAndValues)
            except:
                values.append([colsAndValues])
            # print(colsAndValues)
        return number_of_lines, values


def definire_matrice_rara_dict(file_name):

    number_of_lines = 0  # number of lines in the matrix
    with open(file_name, "r") as f:
        # first line represents the number of lines in the file
        number_of_lines = int(f.readline())
        # create a list with the number of lines
        values = []
        # iterate throw all the lines
        # and append the values in the list
        # print(values)
        colsAndValuesDict = {}
        myDict = {}
        for index, line in enumerate(f):
            line = line.strip().split(',')
            try:
                colsAndValuesDict[int(line[1])][int(line[2])] = float(line[0])
            except:
                colsAndValuesDict[int(line[1])] = {
                    int(line[2]): float(line[0])}
        return number_of_lines, colsAndValuesDict


# n, a = definire_matrice_rara_dict(r"D:\Repo\Facultate3Sem2\CN\a_1.txt")
# print(a[0][31024])


def citire_b(file_name):
    """
    It reads a file and returns a list of floats

    Parameters:
    -----------

    :param file_name: the name of the file to read from

    Returns:
    --------
    :return: A list of floats.
    """
    with open(file_name, "r") as f:
        number_of_lines = int(f.readline())
        b = []
        for index, line in enumerate(f):
            try:
                line = line.strip()
                b.append(float(line))
            except:
                log("Error while converting to float",
                    "definire_matrice_rara", warning=True)
                log(line, f"{index}", warning=True)
        print(b)
        return b


# n, A = definire_matrice_rara(r"D:\Repo\Facultate3Sem2\CN\a_1.txt")
# b = citire_b(r"D:\Repo\Facultate3Sem2\CN\b_1.txt")


def get_element_from_matrix(A, i, j):
    """
    It returns the element from the matrix A at the position (i,j).

    Parameters:
    -----------

    :param A: The matrix to be searched.
    :param i: The line of the element.
    :param j: The column of the element.

    Returns:
    --------
    :return: The element from the matrix A at the position (i,j).
    """
    for element in A[i]:
        if element[1] == j:
            return element[0]
    return 0


# test
# print(get_element_from_matrix(A, 1, 1))


def get_epsilon(n):
    """
    It returns the epsilon value.

    :param n: The number of lines in the matrix.
    :return: The epsilon value.
    """
    return 10**(-n)


def verificare_diagonala_principala(A, n):
    """
    It verifies if the matrix is diagonally dominant.

    :param A: The matrix to be verified.
    :param n: The number of lines in the matrix.
    :return: True if all the values from the main diagonal are greater then 0( greater than epsilon), False otherwise.
    """
    # epsilon in utf-8
    ε = get_epsilon(7)
    for i in range(n):
        if get_element_from_matrix(A, i, i) < ε:
            return False
    return True


def gauss_seidel2(A, b, n, x0, eps=1e-7, kmax=10000):
    xc = x0
    k = 0
    delta_x = eps + 1
    while delta_x >= eps and k < kmax and delta_x <= 1e8:
        print('iteration', k)
        delta_x = 1
        # delta_x = eps + 1
        for i in tqdm(range(n)):
            s1 = 0
            s2 = 0
            for j in range(n):
                try:
                    element = A[i][j]
                except:
                    element = 0
                if j < i:
                    if (element != 0):
                        s1 += element * xc[j]
                if j > i:
                    if (element != 0):
                        s2 += element * xc[j]
            x_new = (b[i] - s1 - s2) / A[i][i]
            x_last = xc[i]
            normal_form = pow(x_new - x_last, 2)
            delta_x = math.sqrt(normal_form)
            xc[i] = x_new
            k += 1
    if delta_x < eps:
        log(f"Convergena la {k} iteratii", "gauss_seidel")
        log(f"The approximate solution is {xc}", "gauss_seidel")
        with open(r"D:\Repo\Facultate3Sem2\CN\output.txt", "w") as f:
            f.write(f"xc = {xc}")
        return xc
    else:
        log("Divergenta", "gauss_seidel", error=True)
        return None


def gauss_seidel_3(a, f, n, p, q):
    # initiere vector x
    x = [0.0] * n
    delta_x = 1
    epsilon = 10 ** (-13)
    k_max = 10000
    k = 0

    # conditiile de terminare
    while (k <= k_max) and (delta_x >= epsilon) and (delta_x <= 10 ** 13):
        elem_diag = 1.0

        for i in range(0, n):
            suma1 = 0.0
            suma2 = 0.0

            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j == i - p:
                    suma1 += x[j] * a[i][j]
                elif j == i + q:
                    suma2 += a[i][j] * x[j]
                if j == i:
                    elem_diag = a[i][j]

            x_curent = (f[i] - suma1 - suma2) / elem_diag
            x_anterior = x[i]

            # calcul norma
            norma = pow(x_curent - x_anterior, 2)
            delta_x = math.sqrt(norma)

            x[i] = abs(x_curent)
            k += 1
    return x


def gauss_seidel(A, b, n, x0, eps=1e-7, kmax=10000):
    xc = x0
    k = 0
    delta_x = eps + 1
    while delta_x >= eps and k < kmax and delta_x <= 1e8:
        print('iteration', k)
        delta_x = 0
        # delta_x = eps + 1
        for i in tqdm(range(n)):
            xp = xc[i]
            s = 0
            for j in range(n):
                if j != i:
                    # element = get_element_from_matrix(A, i, j)
                    try:
                        element = get_element_from_matrix(A, i, j)
                    except Exception as e:
                        element = 0
                    if (element != 0):
                        s += element * xc[j]

            diag = get_element_from_matrix(A, i, i)
            xc[i] = float(float(b[i] - s) / diag)
            delta_x = math.sqrt((pow(xc[i]-xp, 2)))
            # delta_x = math.sqrt(max(delta_x, abs(xc[i] - xp)))
            # log(f"delta_x = {delta_x}", "gauss_seidel")
            k += 1
            if delta_x <= eps or k > kmax or delta_x > 1e8:
                break
    if delta_x < eps:
        log(f"Convergena la {k} iteratii", "gauss_seidel")
        log(f"The approximate solution is {xc}", "gauss_seidel")
        with open(r"D:\Repo\Facultate3Sem2\CN\output.txt", "w") as f:
            f.write(f"xc = {xc}")
        return xc
    else:
        log("Divergenta", "gauss_seidel", error=True)
        # return None
        return xc
# gauss_seidel(A,b,n)


def generate_0_array(n):
    return np.array([0.0 for _ in range(n)], dtype='f')


x0 = [1.0, 2.0, 3.0, 4.0, 5.0]
b = [6.0, 7.0, 8.0, 9.0, 1.0]
x0 = [0, 0, 0, 0, 0]
n, A = definire_matrice_rara(r"D:\Repo\Facultate3Sem2\CN\a_5.txt")
b = citire_b(r"D:\Repo\Facultate3Sem2\CN\b_5.txt")
x0 = generate_0_array(n)

log(f"A = {A}", "main")
log(f"b = {b}", "main")
log(f"x0 = {x0}", "main")
# A, b, n, x0=[0 for _ in range(n)], eps=1e-7, kmax=10000
rezz = gauss_seidel(A, b, n, x0)
log(f"{rezz}", "gauss_seidel_Answer")


def norma(A, x, result, n):
    x = np.array(x)
    b = generate_0_array(n)
    # calculez Ax
    log("Calculul Ax", "norma")
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += get_element_from_matrix(A, i, j)*x[j]
        b[i] = suma
    log(f"{b}", "norma")
    # calculez result - Ax
    log("Calculul result - Ax", "norma")
    log(f"{result}", "norma")
    log(f"{b}", "norma")
    res = np.subtract(result, b)

    return np.linalg.norm(res, np.inf)


print(norma(A, rezz, b, n))
# n, A = definire_matrice_rara(r"D:\Repo\Facultate3Sem2\CN\exercitiu.txt")
# b = [6.0, 7.0, 8.0, 9.0, 1.0]
