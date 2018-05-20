#!/usr/bin/env python3
# pip3 install --user http://bit.ly/csc161graphics

import sys
import os.path
from graphics import *

width = 800
height = 800

fileindex = 1

def checkFile():
	global fileindex
	while os.path.isfile('points' + str(fileindex) + '.txt'):
		fileindex += 1


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def main():

    checkFile()

    x = []
    y = []

    win = GraphWin('Press Save & Exit, save file: ' + 'points' + str(fileindex) + '.txt', width, height)
    #win.yUp() # right side up coordinates
    win.setBackground('white')

    
    quit = Rectangle(Point(width / 2 - 55, height - 40), Point(width / 2 + 55, height - 5))
    quit.draw(win)
    quit.setFill("red")
    text = Text(Point(width / 2, height - 20), "Save & Exit")
    text.draw(win)

    #message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    #message.setTextColor('red')
    #message.setStyle('italic')
    #message.setSize(20)
    #message.draw(win)

    count = 0
    while True:
        p = win.getMouse()

        if inside(p, quit):
        	break
        # print(p.x, p.y)
        c = Circle(Point(p.x,p.y), 1)
        c.draw(win)
        x.append(p.x)
        y.append(p.y)
        count += 1

        white = Rectangle(Point(0, 0), Point(40, 20))
        white.draw(win)
        white.setFill("white")

        countText = Text(Point(10, 10), str(count))
        countText.draw(win)

    if len(x) > 0:
        f = open('points' + str(fileindex) + '.txt', 'w')
        count = len(x)
        for i in range(count):
            f.write(str(x[i]) + ", " + str(y[i]) + '\n')
        f.close()

    win.close()


main()
