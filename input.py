import numpy as np
import cv2
import webcolors
cap = cv2.VideoCapture(0)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

make_720p()


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


while 1:
    ret, img = cap.read()

    
    cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), 2)

    cv2.rectangle(img, (200, 300), (300, 400), (0, 255, 0), 2)

    cv2.rectangle(img, (200, 400), (300, 500), (0, 255, 0), 2)


    cv2.rectangle(img, (300, 200), (400, 300), (0, 255, 0), 2)

    cv2.rectangle(img, (300, 300), (400, 400), (0, 255, 0), 2)

    cv2.rectangle(img, (300, 400), (400, 500), (0, 255, 0), 2)


    cv2.rectangle(img, (400, 200), (500, 300), (0, 255, 0), 2)

    cv2.rectangle(img, (400, 300), (500, 400), (0, 255, 0), 2)

    cv2.rectangle(img, (400, 400), (500, 500), (0, 255, 0), 2)

    cv2.imshow('img',img)

    B,G,R = img[250,250]

    requested_colour = (R, G, B)
    actual_name, closest_name = get_colour_name(requested_colour)

    print(closest_name)
        
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
