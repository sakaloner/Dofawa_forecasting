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

### almas ####
pyautogui.click(87,351)
pyautogui.click(86,379)


##### recursos  ###########
# 200 es un buen scroll
## get a ss of reference for the end of the end of scrolling
im_finished = pyautogui.screenshot(region=(66,166, (300-70), (212-166)))
#im_finished.show()

pyautogui.moveTo(x=218, y=385)
# for i in range(13):
#     pyautogui.scroll(200)
#     time.sleep(0.5)
# for t in range(2):
#     pyautogui.scroll(200)
#     time.sleep(1)
pyautogui.scroll(-20000)

ss_arriba = 0
counter = 0
for i in range(15):
    ss_arriba = pyautogui.screenshot(region=(66,166, (300-70), (212-166)))
    counter +=1
    for i in range(3):
        pyautogui.click(85,(788-(i*30)))
        time.sleep(0.1)
    time.sleep(0.7)
    pyautogui.scroll(200)

for i in range(0, 14):
    time.sleep(0.2)
    pyautogui.click(85,(788-(2*30)-(i*29))) 
exit()

# while 
# pyautogui.click(85,786)



# # ss of last obj in list to see if it can be scrolled more or if it is the end
# last_obj = pyautogui.screenshot(region=(320, 757, 550, 43.3))
# # scrolling
# pyautogui.moveTo(516,615)
# # -120 es el scroll minimo (mueve 3 objetos)
# pyautogui.scroll(-120)
# end_check = pyautogui.screenshot(region=(320, 757, 550, 43.3))
# # updatar cuenta
# count += 3
# # BREAK if it gets to the end
# if end_check == last_obj:
#     break
# #end_check.show()










### armas #####

# abrir tienda
pyautogui.click(259,402)
time.sleep(1)

pos_categories = [
    (98,296),
    (156,285),
    (205,278),
    (262,282),
    (99,347),
    (151,341),
    (199,330),
    (259,329),
    (101,391),
    (156,384),
    (199,390)
]
for pos in pos_categories:  
    pyautogui.click(pos[0], pos[1])
## cerrar tienda
pyautogui.click(1208,83)
