#! /usr/bin/env python3
import cube
import math
def parser_cube2solver(config):
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

