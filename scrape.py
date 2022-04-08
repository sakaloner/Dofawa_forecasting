import pyautogui, time, random
from PIL import Image
import os
from icecream import ic
from marcar_categorias import marcar_casillas
from ss_items import get_items


def move_character():
    # failsafe
    pyautogui.FAILSAFE= True
    #  stop after each call
    pyautogui.Pause = 2.5

    ## activate dofus windows
    dw = pyautogui.getWindowsWithTitle('dofus')
    dw[0].activate()

    ## coordenadas para cambiar de area
    wu = (600,30) # walk up
    wd =  (690,860) # walk down
    wr = (1250, 400) # walk righ
    wl = (20,500)   # walk left
    
    ## espera entre comandos
    tiempo_espera = 9

    ################### moverse a los mercadillos lugares ###################
    ## cordenadas para hacer click en tiendas y entradas de estas
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
    
    ## empieza en el mercadillo de equipables
    ## 7 lugares de tiendas
    ## puede ir en direccion reversa o no
    cordenadas = [
       #[(coor_tiendas['nombre tienda']), steps]
        [coor_click['equipables'], [wd, wd]],
        [coor_click['consumibles'], [wu,wr]],
        [coor_click['recursos'], [wl,wu,wr,wr,wu,wu]],
        [coor_click['runas'], [wu,wu,wl]],
        [coor_click['animales'], [wd,wl,wl,wu,coor_click['almas_ent']]],
        [coor_click['almas'], [coor_click['almas_sal'],wu,wl,wl,wl,coor_click['cosme_ent']]],
        [coor_click['cosmeticos'], [coor_click['cosme_sal'],wr,wr,wd,wd,wr,wd,wd,wr,wd]],              
    ]
    
    inverses = {
    wu: wd,
    wd: wu,
    wr: wl,
    wl: wr,
    coor_click['almas_ent']:coor_click['almas_sal'],
    coor_click['almas_sal']:coor_click['almas_ent'],
    coor_click['cosme_ent']:coor_click['cosme_sal'],
    coor_click['cosme_sal']:coor_click['cosme_ent']
    }
    
    def invertir(direccion):
        if direccion in inverses:
            return inverses[direccion]
        else:
            return direccion
    
    
    def caminar(corde, alrevez=False):
        contador = 0
        ic(corde)
        if alrevez:
            #ic(corde[0])
            corde = corde[::-1]
            ## little fix to get up stairs (wup doesnt work there but wdown does from the other side)
            #print('tiendas',[x[0] for x in corde)
            
            for lugar in corde:
                ic(lugar)
                print('No hay reverso aun')
                exit()
                ## abrir tienda
                #pyautogui.click(lugar[0])
                ## wait until the interface loads
                #time.sleep(5)
                ### falta funcion para marcar casillas ###
                # cerrar tienda
                #pyautogui.click(1208,80)
                #time.sleep(3)

                ### invertir lista de caminar y caminar
                camino_revez = list(map(invertir ,lugar[1][::-1]))
                for step in camino_revez:
                    ic(step)
                    pyautogui.click(step[0], step[1])
                    print('click')
                    contador += 1
                    ic(contador)
                    time.sleep(tiempo_espera)

                ## click en la tienda
                contador = 0
                lugar_tienda = lugar[0]
                ic(lugar_tienda)
                print('click tienda')
                # click tienda
                #pyautogui.click(lugar[0][0], lugar[0][1])
                # Funcion para marcar las casillas de objetos

                # cerrar tienda
                pyautogui.click(1208,80)
        else:
            for lugar in corde[:]:
                ## click en la tienda
                pyautogui.click(lugar[0])
                ## wait until the interface loads
                time.sleep(3)
                ### marcar casillas importada
                marcar_casillas(lugar[0])
                time.sleep(2)
                ### falta funcion para marcar scrapear ###
                get_items()
                time.sleep(2)
                # cerrar tienda
                pyautogui.click(1208,80)
                time.sleep(3)
                ## mover personaje
                for h, step in enumerate(lugar[1]):
                    print('step mini -- ', h+1)
                    ic(step)
                    pyautogui.click(step)
                    contador += 1
                    time.sleep(tiempo_espera)
                ## click en la tienda
                contador = 0
                print(contador)
                #pyautogui.click(lugar[0][0], lugar[0][1])
            
    # Iniciar ruta aleatoriamente
    #inver = random.choice([True, False])
    sentido_invertido = False # provisional
    ic(sentido_invertido)
    caminar(cordenadas, sentido_invertido)


try:
    move_character()
except pyautogui.FailSafeException:
    pyautogui.alert(text='Fail Safed', title='Fail Safe', button='OK')



