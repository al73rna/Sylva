__author__ = 'Al73rnA'

import numpy as np
import cv2
from PIL import ImageGrab,Image
from time import sleep

def img(str):
    return cv2.imread(str)

def find(tmp,_TH=0.9):
    img = np.array(ImageGrab.grab())
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    res = cv2.minMaxLoc(cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED))
    top = res[3]
    center = (top[0]+int(tmp.shape[1]/2),top[1]+int(tmp.shape[0]/2))
    if(res[1]>_TH):
        return center
    else:
        return None

def findAll(tmp,_TH=0.99):
    result = []
    img = np.array(ImageGrab.grab())
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
    match = np.where(res >= _TH)
    for pt in zip(*match[::-1]) :
        result.append((pt[0]+int(tmp.shape[1]/2),pt[1]+int(tmp.shape[0]/2)))
    if len(result)>0 :
        return result
    else:
        return None

def exists(tmp,_TH=0.9):
    if(find(tmp,_TH)!=None):
        return True
    else:
        return False

def waitFor(tmp,_timer="inf",_TH=0.9):
    if _timer == "inf":
        while(not exists(tmp,_TH)):
            sleep(0.5)
    else:
        timer =_timer
        while(timer>=0 and not exists(tmp,_TH)):
            sleep(0.2)
            timer -= 0.2

def waitUntil(tmp,_timer="inf",_TH=0.9):
    if _timer == "inf":
        while(exists(tmp,_TH)):
            sleep(0.5)
    else:
        timer =_timer
        while(timer>=0 and exists(tmp,_TH)):
            sleep(0.2)
            timer -= 0.2
