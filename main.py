from scrape import *
from reading_im import *
from databasear import *
import os


try:
    move_character()
except pyautogui.FailSafeException:
    pyautogui.alert(text='Fail Safed', title='Fail Safe', button='OK')

reading_im()
databasear()
os.remove('objetos.csv')

### erase objetos folders

