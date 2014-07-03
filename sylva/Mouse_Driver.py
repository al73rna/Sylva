
import ctypes
user32 = ctypes.windll.user32
def mouseClick(pos):
    x = pos[0]
    y = pos[1]

    user32.SetCursorPos(x, y)
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    user32.mouse_event(0x0004, 0, 0, 0,0)

def mouseRClick(pos):
    x = pos[0]
    y = pos[1]

    user32.SetCursorPos(x, y)
    user32.mouse_event(0x0008, 0, 0, 0, 0)
    user32.mouse_event(0x0010, 0, 0, 0,0)

def mouseDoubleClick(pos):
    x = pos[0]
    y = pos[1]

    user32.SetCursorPos(x, y)
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    user32.mouse_event(0x0004, 0, 0, 0,0)
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    user32.mouse_event(0x0004, 0, 0, 0,0)

def mouseDragDrop(pos1,pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]

    user32.SetCursorPos(x1, y1)
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    user32.mouse_event(0x0001, x2, y2, 0, 0)
    user32.mouse_event(0x0003, 0, 0, 0, 0)
    user32.mouse_event(0x0004, 0, 0, 0, 0)

def mouseHover(pos):
    x = pos[0]
    y = pos[1]
    user32.SetCursorPos(x, y)
    user32.mouse_event(0x0001, x, y, 0, 0)




mouseHover((10,10))
mouseClick((0,0))