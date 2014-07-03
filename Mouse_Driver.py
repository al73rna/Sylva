__author__ = 'Al73rnA'

import ctypes

def mouseClick(xPos,yPos):
    user32=ctypes.windll.user32
    user32.SetCursorPos(xPos, yPos)
    user32.mouse_event(2, 0, 0, 0, 0)
    user32.mouse_event(4, 0, 0, 0,0)

def mouseDoubleClick(xPos,yPos):
    user32=ctypes.windll.user32
    user32.SetCursorPos(xPos, yPos)
    user32.mouse_event(2, 0, 0, 0, 0)
    user32.mouse_event(4, 0, 0, 0,0)
    user32.mouse_event(2, 0, 0, 0, 0)
    user32.mouse_event(4, 0, 0, 0,0)

