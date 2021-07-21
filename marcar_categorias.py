import pyautogui, time, random
from PIL import Image
import os
from icecream import ic

 # failsafe
pyautogui.FAILSAFE= True
#  stop after each call
pyautogui.Pause = 2.5

## activate dofus windows
dw = pyautogui.getWindowsWithTitle('dofus')
dw[0].activate()

### armas

# abrir tienda
pyautogui.click(259,402)


## cerrar tienda
pyautogui.click(1208,83)