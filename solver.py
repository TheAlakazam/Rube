#! /usr/bin/env python3

from cube import *
import kociemba
import math

def parser(config):
    cubestring = ""
    temp = []
    for i in config:
        if i == 0:
            temp.append("F")
        elif i == 1:
            temp.append("R")
        elif i == 2:
            temp.append("B")
        elif i == 3:
            temp.append("L")
        elif i == 4:
            temp.append("U")
        elif i == 5:
            temp.append("D")
    temp = [temp[i : i + 9] for i in range(0, len(temp), 9)]
    temp2 = []
    temp2.extend(temp[4])
    temp2.extend(temp[1])
    temp2.extend(temp[0])
    temp2.extend(temp[5])
    temp2.extend(temp[3])
    temp2.extend(temp[2])
    cubestring = ''.join(temp2)
    return cubestring
c = Cube()
c.execute("R B' L' R' D2 L' F' D2 B' L2 R2 F2 B' U' L B' D' U R' U' B2 D' L B' U",display = True)
print(c.getConfig())
s = parser(c.getConfig())
print(kociemba.solve(s))
