import pyautogui, time, random
from PIL import Image
import os
from icecream import ic

'''
Bueno se hace una funcion que marque las casillas de la tienda:
def marcar_casillas(nombre_tienda_0_cordenada):
    bla
2 ifs. Si es de marcar casillas sistematicamente o con dibujo.
- para cada marcada de casillas sistematicamente hay una parte general
que es comun a todos los mercadillos pero otra que no.
    - una lista o ifs?
- 
'''

coor_click = {
        # coordenadas en pixeles pantalla de las tiendas
        'equipables':(302,350),
        'consumibles':(807,509),
        'recursos':(1140,424),
        'runas':(1122,559),
        'animales':(944,625),
        'almas':(472,129),
        'almas_ent':(731,372),
        'almas_sal':(255,638),
        'cosmeticos':(788,156),
        'cosme_ent':(925,269),
        'cosme_sal':(229,763)
    }

def marcar_casillas(nom_mercadillo = None):
    ######### Set Up ###########
    # failsafe
    pyautogui.FAILSAFE= True
    #  stop after each call
    pyautogui.Pause = 2.5

    ## activate dofus windows (quitarlo luego)
    dw = pyautogui.getWindowsWithTitle('dofus')
    dw[0].activate()
    
    ## get a ss of reference for the end of the end of scrolling
    im_finished = pyautogui.screenshot(region=(66,166, (300-70), (212-166)))
    #im_finished.show()
    ## Go down until the end of the item list
    pyautogui.moveTo(x=218, y=385)
    pyautogui.scroll(-20000)
    time.sleep(1)
    ### reiniciar casillas
    pyautogui.click(172,813)
    ###### Recursos o consumibles ##########
    if nom_mercadillo in [coor_click['recursos'],coor_click['consumibles']]:
        #### general formula #####
        ## necesita al final arreglos para cada cosa
        
        ss_arriba = 0
        while True:
            ss_arriba = pyautogui.screenshot(region=(66,166, (300-70), (212-166)))
            if ss_arriba == im_finished:
                break
            for i in range(3):
                pyautogui.click(85,(788-(i*30)))
                time.sleep(0.1)
            time.sleep(1)
            pyautogui.scroll(200)
        time.sleep(2)
        if nom_mercadillo == coor_click['recursos']:
            ### end for recursos
            pyautogui.click(88,790)
            for i in range(13):
                time.sleep(0.2)
                pyautogui.click(85,(788-(3*30)-(i*29)))
        else: ## final consumibles
            for i in range(6):
                time.sleep(0.2)
                pyautogui.click(85,(788-(1*30)-(i*29)))
    if nom_mercadillo == coor_click['equipables'] :
        pos_categories = [
            (98,296),(156,285),(205,278),(262,282),(99,347),(151,341),
            (199,330),(259,329),(101,391),(156,384),(199,390)
        ]
        for pos in pos_categories:  
            pyautogui.click(pos[0], pos[1])

    if nom_mercadillo == coor_click['runas']:
        for i in range(6):   
            time.sleep(0.2)
            pyautogui.click(85,(496-(i*29)))

    if nom_mercadillo == coor_click['animales']:
        for i in range(5):   
            time.sleep(0.2)
            pyautogui.click(85,(471-(i*29)))

    if nom_mercadillo == coor_click['almas']:
        pyautogui.click(85,380)
        pyautogui.click(85,351)
    
    if nom_mercadillo == coor_click['cosmeticos']:
        for i in range(14):
            if i in [3,5]:
                continue   
            time.sleep(0.2)
            pyautogui.click(85,(727-(i*29)))




