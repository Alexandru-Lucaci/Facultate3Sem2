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
    
A = np.array([[1,2.5,3],[2.5,8.25,15.5],[3,15.5,43]])
b = np.array([[1],[2],[2]])