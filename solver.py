#! /usr/bin/env python3

from cube import *
import kociemba
import math
list_of_moves = ['F', 'R', 'L', 'B', 'U', 'D', "F'", "R'", "L'", "B'", "U'", "D'"]
# class GraphNode(object):

    # def __init__(self, conf):
        # self.config = conf
        # self.attached = []
    
    # def move(self, s):
        # c = Cube(config = self.config)
        # c.execute(s)
        # return c.getConfig()
   
   # def generateNeighbours(self):
       # for mv in list_of_moves:
           # newCube = GraphNode(Cube(self.move(mv)).getConfig())
           # self.attached.append(newCube)

# if __name__ == '__main__':
    # input_config = []
    # root = GraphNode(input_config)
    # end = GraphNode(DEFAULT_CONFIG)
    # while genNode.config != end.config:

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
    for k in temp[-18:-9]:
        cubestring += k
    for k in temp[9:18]:
        cubestring += k
    for k in temp[0:9]:
        cubestring += k
    for k in temp[-9:]:
        cubestring += k
    for k in temp[18:27]:
        cubestring += k
    for k in temp[27:36]:
        cubestring += k
    return cubestring
c = Cube()
c.execute("R B' L' R' D2 L' F' D2 B' L2 R2 F2 B' U' L B' D' U R' U' B2 D' L B' U",display = True)
print(c.getConfig())
s = parser(c.getConfig())
print(s)
print(kociemba.solve("RLDLUBUBRDRFDRFUDBFUFLFRRUBFRLBDFBBRUULRLFDLULDBUBFDDL"))
