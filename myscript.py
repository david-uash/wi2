#!/usr/local/bin/python


import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("numpy")
import numpy
a = np.zeros(2,2)
print(a)
