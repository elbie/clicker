#! /usr/bin/python

import sys
import time
from Quartz.CoreGraphics import *

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy),
                                       kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy)

def mouseclick(posx,posy):
    mouseEvent(kCGEventLeftMouseDown, posx,posy)
    mouseEvent(kCGEventLeftMouseUp, posx,posy)

def clicklots(x=1000, y=600, l=100000, z=0.02):
    mousemove(x, y)
    # The system may need a moment to catch up before actually getting
    # current position.  You may need to adjust this sleep interval
    # accordingly, or just start with your mouse cursor in the
    # "correct" position
    time.sleep(0.1)
    for i in range(0, l):
        # Check how far we've moved
        loopEvent = CGEventCreate(None)
        currentpos = CGEventGetLocation(loopEvent)
        #print('X: ' + str(int(currentpos.x)) + ', Y: ' + str(int(currentpos.y)))
        if abs(currentpos.x - x) > 20:
            #print('Strayed outside of X constraint after click ' + str(i))
            break
        if abs(currentpos.y - y) > 20:
            #print('Strayed outside of Y constraint after click ' + str(i))
            break
        mouseclick(int(currentpos.x),int(currentpos.y))
        time.sleep(z)

if __name__ == '__main__':
    clicklots()
