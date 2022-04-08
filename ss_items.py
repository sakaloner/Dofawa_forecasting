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
def get_items():
    # dummy values
    count = 0 

    while True:
        ### first pass ###
        # take the screenshots
        todo = pyautogui.screenshot(region=(320, 195, 550, 130))
        # individual crops
        uno = todo.crop((0,0,550,43))
        dos = todo.crop((0,43,550,86.5))
        tres = todo.crop((0,86.5,550,130))
        
        # crear primer carpeta con la fecha
        fecha = time.gmtime()
        nombre_carpeta = f'objetos-{fecha.tm_mday}_{fecha.tm_mon}_{fecha.tm_year}'
        os.makedirs(nombre_carpeta, exist_ok=True)
        # guardar
        uno.save(f'{nombre_carpeta}/{count+1}.png')
        dos.save(f'{nombre_carpeta}/{count+2}.png')
        tres.save(f'{nombre_carpeta}/{count+3}.png')

        
        # ss of last obj in list to see if it can be scrolled more or if it is the end
        last_obj = pyautogui.screenshot(region=(320, 713, 550, 86.6))
        # scrolling
        pyautogui.moveTo(516,615)
        # -120 es el scroll minimo (mueve 3 objetos)
        pyautogui.scroll(-120)
        time.sleep(0.5)
        end_check = pyautogui.screenshot(region=(320, 713, 550, 86.6))
        # updatar cuenta
        count += 3
        # BREAK if it gets to the end
        if end_check == last_obj:
            break
        #end_check.show()

    ## cuando llega a la ventana final
    todo_final = pyautogui.screenshot(region=(320, 325, 550, 473))
    for i in range(11):
        todo_final.crop((0,(i*43),550,(43+(i*43)))).save(f'{nombre_carpeta}/{count+1+i}.png')
time.sleep(2)
get_items()