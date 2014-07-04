from core import *
import KeyBD_Driver
import Mouse_Driver

ax = img("ax2.png")
waitFor(ax)
Mouse_Driver.mouseClick(find(ax))
KeyBD_Driver.typeString("")