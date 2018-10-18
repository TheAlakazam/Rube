# Rube
-----------
Rubiks cube solver using OpenCV. Uses OpenGL for 3D Representation of the code.

## Requirements ##
  * Python 3
  * OpenGL
  
## Installation Instructions ##

It's preferred and better if you use a **virtual environment** for using this project so that your system dependencies are not messed up by installing the required packages.
Recommended using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest) creating virtual environments (on Linux).

+ Install Python Packages

``` bash
git clone https://github.com/TheAlakazam/Rube.git
cd Rube
[sudo] pip install -r requirements.txt
```
+ Run Program

``` bash
python3 main.py
```

+ Instructions
  + First place Face with Red center in front of the camera in the region outlined
  + Go in the order R, B, O, G, W, Y by turning it one by one.
    + With RED in front facing the camera, turn the cube one by one clockwise till you reach RED again
    + For WHITE turn the cube from RED facing forward down to have WHITE face forward
    + For YELLOW after WHITE turn twice in downward direction to get YELLOW.
    + Press space to input the configuration
  + After entering all 6 sides, the window bottom left shows number of sides having input.
  + Press ESC to quit the camera input.
  + Incase the input was invalid and did not contain all the sides the program loads a random scramble and solves it.
  + It takes time for the 3D cube to start moving.

## References ##

+ [Rubiks OpenGL Implementation](https://github.com/gillima/Rubiks)
+ [Kociemba's Algorithm](http://kociemba.org/cube.htm) 
+ [Color Detection](https://github.com/dwalton76/rubiks-cube-tracker-Andrej-Karpathy/blob/master/525report.pdf)

