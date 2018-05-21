#!/usr/bin/env python3

# pip3 install --user http://bit.ly/csc161graphics

import sys
import os.path
from graphics import *
from forel import FOREL
points = []
filename = ""

width = 400
height = 400

def readpoints():
    global points
    global filename
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        sys.exit(1)
    with open(filename) as f:
        content = f.readlines()
    points = [list(map(float, x.strip().split(','))) for x in content]

def getclusters():
    global points

    forel = FOREL()

    # size choise
    size = 10
    r_min = 0
    r_max = ()
    return [(100, 100, 20), (200, 200, 30)]


def drawpoints():
    global points
    global width
    global height
    global filename
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])    
    width = width if max_x < width else max_x + 50
    height = height if max_y < height else max_y + 50
    
    win = GraphWin('Points loaded from ' + filename, width, height)

    for x in points:
        c = Circle(Point(int(x[0]), int(x[1])), 1)
        c.draw(win)

    clusters = getclusters()

    for cluster in clusters:
        c = Circle(Point(int(cluster[0]), int(cluster[1])), 1)
        c.draw(win)
        c.setOutline('red')
        c = Circle(Point(int(cluster[0]), int(cluster[1])), int(cluster[2]))
        c.draw(win)
        c.setOutline('red')



    win.getMouse()

    win.close()


def main():

    readpoints()

    drawpoints()

    

main()
