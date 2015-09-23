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
    """ clicks lots """
    mousemove(x, y)
    time.sleep(0.1)
    for i in range(0, l):
        # Check how far we've moved
        loopEvent = CGEventCreate(None)
        currentpos = CGEventGetLocation(loopEvent)
        if abs(currentpos.x - x) > 20:
            #print('Strayed outside of X constraint after click ' + str(i))
            break
        if abs(currentpos.y - y) > 20:
            #print('Strayed outside of Y constraint after click ' + str(i))
            break
        mouseclick(int(currentpos.x),int(currentpos.y))
        time.sleep(z)

def currentpos():
    """ grabs the current mouse position, and prints the function call
        for clicklots with the position filled in.  Returns the position
        as a tuple """
    loopEvent = CGEventCreate(None)
    currentpos = CGEventGetLocation(loopEvent)
    print 'clicker.clicklots(x=' + str(int(currentpos.x)) + ',y=' + str(int(currentpos.y)) + ')'
    return(int(currentpos.x),int(currentpos.y))

if __name__ == '__main__':
    (x,y) = currentpos()
    clicklots(x=x,y=y)
