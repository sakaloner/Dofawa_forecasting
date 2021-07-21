import pyautogui, time, random
from PIL import Image
import os
from icecream import ic

def move_character():
    # failsafe
    pyautogui.FAILSAFE= True
    #  stop after each call
    pyautogui.Pause = 2.5

    ## activate dofus windows
    dw = pyautogui.getWindowsWithTitle('dofus')
    dw[0].activate()

    ## coordenadas para cambiar de area
    wup = (600,30)
    wdown =  (690,860)
    wright = (1250, 400)
    wleft = (20,500)
    
    ## espera entre comandos
    tiempo_espera = 8
    ################### moverse a los mercadillos lugares ###################
    ## empieza en el de armas
    ## recursos
    cordenadas = [
       #[(coordinate_store), steps]
        [(645,470), [wleft, wleft, wleft, wup, wup]],   #recursos
        [(237,395), [wup, wleft, wleft, wup]],          #runas
        [(144,318), [wleft, wleft, wleft, wleft, wup]],  #animales
        [(508,233), [wup, wright, wright, wright, wright, (805,404)]], #almas                                   
        [(558,492), [(202,777), wup, wup, wup, wright, wright]],  #consumibles
        [(240,368), [wdown,wdown,wdown, wdown, wdown, wright, wright,wdown,wdown,wdown,wdown,wright]] #armas                                       
    ]
    coordenadas_tiendas = [
        (240,368), # armas
        (645,470), # recurso
        (237,395),
        (144,318),
        (508,233),
        (558,492),
        (240,368)
    ]
    inverses = {
    wup: wdown,
    wdown: wup,
    wright: wleft,
    wleft: wright,
    (202,777): (805,404), # coliseo/almas
    (805,404): (202,777)  # coliseo/almas
    }
    def invertir(direccion):
        if direccion in inverses:
            return inverses[direccion]
        else:
            return direccion
    
    
    def caminar(corde, alrevez=False):
        contador = 0
        if alrevez:
            corde = corde[::-1]
            for lugar in corde:
                camino_revez = list(map(invertir ,lugar[1][::-1]))
                ic(camino_revez)
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
            for lugar in corde:
                for step in lugar[1]:
                    print()
                    pyautogui.click(step[0], step[1])
                    contador += 1
                    time.sleep(tiempo_espera)
                ## click en la tienda
                contador = 0
                #pyautogui.click(lugar[0][0], lugar[0][1])
            
    # Iniciar ruta aleatoriamente
    rand = random.choice([True, False])
    print('rand=', rand)
    caminar(cordenadas, rand)



move_character()
exit()

def scrape():
    # import pyautogui, time
    # from PIL import Image
    # import os

    
    pyautogui.Pause = 2.5

    # get the dofus window
    dw = pyautogui.getWindowsWithTitle('dofus')
    dw[0].activate()

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

        # crear primer carpeta con el año
        fecha = time.gmtime()
        nombre_carpeta = f'objetos-{fecha.tm_mday}_{fecha.tm_mon}_{fecha.tm_year}'
        os.makedirs(nombre_carpeta, exist_ok=True)
        # guardar
        uno.save(f'{nombre_carpeta}/{count+1}.png')
        dos.save(f'{nombre_carpeta}/{count+2}.png')
        tres.save(f'{nombre_carpeta}/{count+3}.png')

        
        # ss of last obj in list to see if it can be scrolled more or if it is the end
        last_obj = pyautogui.screenshot(region=(320, 757, 550, 43.3))
        # scrolling
        pyautogui.moveTo(516,615)
        # -120 es el scroll minimo (mueve 3 objetos)
        pyautogui.scroll(-120)
        end_check = pyautogui.screenshot(region=(320, 757, 550, 43.3))
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

    pyautogui.alert('done')
scrape()