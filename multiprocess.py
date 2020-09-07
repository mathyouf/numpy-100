import multiprocessing
from time import sleep
import numpy as np

def sleepSorter(n):
    sleep(n)
    print(n, end=", ")

def sleepsort(listToSort):
    for n in listToSort:
        p = multiprocessing.Process(target=sleepSorter, args=(n, ))
        p.start()

目録 = np.random.randint(1, 101, 45)

print("input     = \t", 目録)
print("Should be = \t",   sorted(目録))
print("Sleepsort = \t [", end="")
sleepsort(目録)
input()