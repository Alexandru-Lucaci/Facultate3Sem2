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
        print(number_of_lines)
        # create a list with the number of lines
        values = []
        # iterate throw all the lines
        # and append the values in the list
        print(values)
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


n, A = definire_matrice_rara(r"D:\Repo\Facultate3Sem2\CN\a_1.txt")
b = citire_b(r"D:\Repo\Facultate3Sem2\CN\b_1.txt")


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
    return -1


# test
print(get_element_from_matrix(A, 1, 1))


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


# print(verificare_diagonala_principala(A, n))