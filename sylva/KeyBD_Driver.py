__author__ = 'Al73rnA'

import ctypes
from time import sleep

keyDic={
    '0' : 0x30 ,
    '1' : 0x31 ,
    '2' : 0x32 ,
    '3' : 0x33 ,
    '4' : 0x34 ,
    '5' : 0x35 ,
    '6' : 0x36 ,
    '7' : 0x37 ,
    '8' : 0x38 ,
    '9' : 0x39 ,
    'a' : 0x41 ,
    'b' : 0x42 ,
    'c' : 0x43 ,
    'd' : 0x44 ,
    'e' : 0x45 ,
    'f' : 0x46 ,
    'g' : 0x47 ,
    'h' : 0x48 ,
    'i' : 0x49 ,
    'j' : 0x4A ,
    'k' : 0x4B ,
    'l' : 0x4C ,
    'm' : 0x4D ,
    'n' : 0x4E ,
    'o' : 0x4F ,
    'p' : 0x50 ,
    'q' : 0x51 ,
    'r' : 0x52 ,
    's' : 0x53 ,
    't' : 0x54 ,
    'u' : 0x55 ,
    'v' : 0x56 ,
    'w' : 0x57 ,
    'x' : 0x58 ,
    'y' : 0x59 ,
    'z' : 0x5A ,
    'LBUTTON': 0x01 ,                 # Left mouse button
    'RBUTTON': 0x02,                 # Right mouse button
    'CANCEL': 0x03 ,                   # Control-break processing
    'MBUTTON': 0x04 ,               # Middle mouse button (three-button mouse)
    'XBUTTON1': 0x05 ,              # X1 mouse button
    'XBUTTON2': 0x06 ,              # X2 mouse button
    'BACK': 0x08 ,                        # BACKSPACE key
    'TAB': 0x09 ,                          # TAB key
    '    ': 0x09 ,                          # TAB key
    'CLEAR': 0x0C ,                      # CLEAR key
    'RETURN': 0x0D ,                   # ENTER key
    'SHIFT': 0x10,                       # SHIFT key
    'CONTROL': 0x11 ,                  # CTRL key
    'MENU': 0x12 ,                       # ALT key
    'PAUSE': 0x13 ,                      # PAUSE key
    'CAPITAL': 0x14 ,                   # CAPS LOCK key
    'KANA': 0x15 ,                        # IME Kana mode
    'HANGUL': 0x15 ,                   # IME Hangul mode
    'JUNJA': 0x17 ,                     # IME Junja mode
    'FINAL': 0x18 ,                      # IME final mode
    'HANJA': 0x19 ,                     # IME Hanja mode
    'KANJI': 0x19 ,                      # IME Kanji mode
    'ESCAPE': 0x1B ,                     # ESC key
    'CONVERT': 0x1C ,                  # IME convert
    'NONCONVERT': 0x1D ,          # IME nonconvert
    'ACCEPT': 0x1E ,                     # IME accept
    'MODECHANGE': 0x1F ,          # IME mode change request
    'SPACE': 0x20 ,                      # SPACEBAR
    ' ': 0x20 ,                      # SPACEBAR
    'PRIOR': 0x21  ,                      # PAGE UP key
    'NEXT': 0x22 ,                        # PAGE DOWN key
    'END': 0x23 ,                          # END key
    'HOME': 0x24 ,                       # HOME key
    'LEFT': 0x25 ,                         # LEFT ARROW key
    'UP': 0x26 ,                             # UP ARROW key
    'RIGHT': 0x27,                       # RIGHT ARROW key
    'DOWN': 0x28 ,                      # DOWN ARROW key
    'SELECT': 0x29  ,                   # SELECT key
    'PRINT': 0x2A  ,                     # PRINT key
    'EXECUTE': 0x2B  ,                 # EXECUTE key
    'SNAPSHOT': 0x2C  ,              # PRINT SCREEN key
    'INSERT': 0x2D ,                    # INS key
    'DELETE': 0x2E  ,                   # DEL key
    'HELP': 0x2F ,                          # HELP key
    'LWIN': 0x5B ,                         # Left Windows key (Natural keyboard)
    'RWIN': 0x5C ,                         # Right Windows key (Natural keyboard)
    'APPS': 0x5D ,                          # Applications key (Natural keyboard)
    'SLEEP': 0x5F  ,                       # Computer Sleep key
    'NUMPAD0': 0x60 ,                  # Numeric keypad 0 key
    'NUMPAD1': 0x61  ,                  # Numeric keypad 1 key
    'NUMPAD2': 0x62 ,                  # Numeric keypad 2 key
    'NUMPAD3': 0x63 ,                  # Numeric keypad 3 key
    'NUMPAD4': 0x64 ,                  # Numeric keypad 4 key
    'NUMPAD5': 0x65 ,                  # Numeric keypad 5 key
    'NUMPAD6': 0x66 ,                  # Numeric keypad 6 key
    'NUMPAD7': 0x67 ,                  # Numeric keypad 7 key
    'NUMPAD8': 0x68 ,                  # Numeric keypad 8 key
    'NUMPAD9': 0x69 ,                  # Numeric keypad 9 key
    'MULTIPLY': 0x6A ,                 # Multiply key
    'ADD': 0x6B ,                           # Add key
    'SEPARATOR': 0x6C ,              # Separator key
    'SUBTRACT': 0x6D ,                # Subtract key
    'DECIMAL': 0x6E  ,                  # Decimal key
    'DIVIDE': 0x6F ,                      # Divide key
    'F1': 0x70  ,                              # F1 key
    'F2': 0x71  ,                              # F2 key
    'F3': 0x72  ,                             # F3 key
    'F4': 0x73  ,                             # F4 key
    'F5': 0x74  ,                             # F5 key
    'F6': 0x75  ,                             # F6 key
    'F7': 0x76  ,                             # F7 key
    'F8': 0x77  ,                             # F8 key
    'F9': 0x78  ,                             # F9 key
    'F10': 0x79 ,                             # F10 key
    'F11': 0x7A  ,                            # F11 key
    'F12': 0x7B ,                             # F12 key
    'F13': 0x7C  ,                            # F13 key
    'F14': 0x7D  ,                            # F14 key
    'F15': 0x7E  ,                            # F15 key
    'F16': 0x7F ,                             # F16 key
    'F17': 0x80  ,                            # F17 key
    'F18': 0x81  ,                             # F18 key
    'F19': 0x82 ,                              # F19 key
    'F20': 0x83 ,                             # F20 key
    'F21': 0x84  ,                             # F21 key
    'F22': 0x85  ,                             # F22 key
    'F23': 0x86  ,                             # F23 key
    'F24': 0x87   ,                            # F24 key
    'NUMLOCK': 0x90  ,                   # NUM LOCK key
    'SCROLL': 0x91  ,                       # SCROLL LOCK key
    'LSHIFT': 0xA0   ,                     # Left SHIFT key
    'RSHIFT': 0xA1    ,                    # Right SHIFT key
    'LCONTROL': 0xA2 ,                  # Left CONTROL key
    'RCONTROL': 0xA3  ,                 # Right CONTROL key
    'LMENU': 0xA4   ,                      # Left MENU key
    'RMENU': 0xA5   ,                                   # Right MENU key
    'BROWSER_BACK': 0xA6 ,                      # Browser Back key
    'BROWSER_FORWARD': 0xA7 ,              # Browser Forward key
    'BROWSER_REFRESH': 0xA8 ,               # Browser Refresh key
    'BROWSER_STOP': 0xA9  ,                    # Browser Stop key
    'BROWSER_SEARCH': 0xAA ,                 # Browser Search key
    'BROWSER_FAVORITES': 0xAB ,           # Browser Favorites key
    'BROWSER_HOME': 0xAC ,                    # Browser Start and Home key
    'VOLUME_MUTE': 0xAD ,                       # Volume Mute key
    'VOLUME_DOWN': 0xAE ,                      # Volume Down key
    'VOLUME_UP': 0xAF ,                            # Volume Up key
    'MEDIA_NEXT_TRACK' : 0xB0 ,             # Next Track key
    'MEDIA_PREV_TRACK' : 0xB1,               # Previous Track key
    'MEDIA_STOP': 0xB2,                           # Stop Media key
    'MEDIA_PLAY_PAUSE' : 0xB3,              # Play/Pause Media key
    'LAUNCH_MAIL ': 0xB4,                       # Start Mail key
    'LAUNCH_MEDIA_SELECT' : 0xB5,      # Select Media key
    'LAUNCH_APP1' : 0xB6,                        # Start Application 1 key
    'LAUNCH_APP2' : 0xB7,                       # Start Application 2 key

    'OEM_1' : 0xBA  ,                   # Used for miscellaneous characters; it can vary by keyboard.
    ';' : 0xBA  ,#  For the US standard keyboard, the ';:' key
    'OEM_PLUS' : 0xBB  ,# For any country/region, the '+' key
    '=' : 0xBB  ,
    'OEM_COMMA' : 0xBC  ,
    ',' : 0xBC  ,# For any country/region, the ',' key
    'OEM_MINUS' : 0xBD   ,        # For any country/region, the '-' key
    '-' : 0xBD   ,        # For any country/region, the '-' key
    'OEM_PERIOD' : 0xBE   ,        # For any country/region, the '.' key
    '.' : 0xBE   ,
    'OEM_2' : 0xBF         ,            # Used for miscellaneous characters; it can vary by keyboard.
    '/' : 0xBF         ,            # For the US standard keyboard, the '/?' key
    'OEM_3' : 0xC0         ,            # Used for miscellaneous characters; it can vary by keyboard.
    '`' : 0xC0         ,                                              # For the US standard keyboard, the '`~' key
    'OEM_4' : 0xDB          ,           # Used for miscellaneous characters; it can vary by keyboard.
    '[' : 0xDB          ,                                              # For the US standard keyboard, the '[{' key
    'OEM_5' : 0xDC           ,          # Used for miscellaneous characters; it can vary by keyboard.
    "\\" : 0xDC           ,
    'OEM_6' : 0xDD          ,           # Used for miscellaneous characters; it can vary by keyboard.
    ']' : 0xDD          ,                                             # For the US standard keyboard, the ']}' key
    'OEM_7' : 0xDE           ,          # Used for miscellaneous characters; it can vary by keyboard.
    "'" : 0xDE           ,                                              # For the US standard keyboard, the 'single-quote/double-quote' key
    'OEM_8' : 0xDF            ,         # Used for miscellaneous characters; it can vary by keyboard.
    'OEM_102' : 0xE2           ,       # Either the angle bracket key or the backslash key on the RT 102-key keyboard
    'PROCESSKEY' : 0xE5         ,   # IME PROCESS key
    'PACKET' : 0xE7          ,           # Used to pass Unicode characters as if they were keystrokes. The     'PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
    'ATTN' : 0xF6             ,           # Attn key
    'CRSEL' : 0xF7            ,          # CrSel key
    'EXSEL' : 0xF8             ,         # ExSel key
    'EREOF' : 0xF9             ,        # Erase EOF key
    'PLAY' : 0xFA              ,        # Play key
    'ZOOM' : 0xFB               ,     # Zoom key
    'PA1' : 0xFD                ,       # PA1 key
    'OEM_CLEAR' : 0xFE          , # Clear key

}
#_______

user32=ctypes.windll.user32

def keyDown(keyName):
    keyCode=keyDic[keyName]
    user32.keybd_event(keyCode,0,0,0)

def keyUp(keyName):
    keyCode=keyDic[keyName]
    user32.keybd_event(keyCode,0,2,0)

def pressKey(keyName):
    keyCode=keyDic[keyName]
    user32.keybd_event(keyCode,0,0,0)
    user32.keybd_event(keyCode,0,2,0)
    sleep(0.05)

chardic = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','-':'_','=':'+','[':'{',
           ']':'}',';':':',"'":'"',',':'<','.':'>','/':'?','\\':'|','`':'~' }

def typeString(str,_interval = 0.05):
    for i in str :
        if(i in "abcdefghijklmnopqrstuvwxyz "):
            keyDown(i)
            keyUp(i)
            sleep(_interval)
        elif i in "ABCDEFGHIJKLMNOPQRTSUVWXYZ":
            keyDown("LSHIFT")
            keyDown(i.lower())
            keyUp(i.lower())
            keyUp("LSHIFT")
            sleep(_interval)
        elif i in chardic.keys():
            keyDown(i)
            keyUp(i)
            sleep(_interval)
        elif i in chardic.values():
            ch = chardic.keys()[chardic.values().index(i)]
            keyDown("LSHIFT")
            keyDown(ch)
            keyUp(ch)
            keyUp("LSHIFT")
            sleep(_interval)
        else:
            raise "not supportet"

