import re
import string

def MultiplicationTable(x:str):
        x = int(x)
        for i in range(1, 11):
                print(x, "x", i, "=", x * i, sep = ' ')
        return 1

def DoubleValue(x:int):
        return x * 2