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
    tiempo_espera = 5
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
        [(240,368), [wright, wright, wdown, wdown, wdown, wdown, wdown, wdown, wdown]] #armas                                       
    ]
    inverses = {
    wup: wdown,
    wdown: wup,
    wright: wleft,
    wleft: wright
    }
    def invertir(direccion):
        ic(direccion)
        return inverses[direccion]
    
    def caminar(corde, alrevez=False):
        if alrevez:
            corde = corde[::-1]
            for lugar in corde:
                for step in lugar[1]:
                    if step in inverses:
                        ic(lugar)
                        ic(step)
                        step = list(map(invertir,step[::-1]))
                        ic(step)
                        pyautogui.click(step[0], step[1])
                        time.sleep(tiempo_espera)
                ## click en la tienda
                pyautogui.click(lugar[0][0], lugar[0][1])
        else:
            for lugar in corde:
                for step in lugar[1]:
                    print()
                    pyautogui.click(step[0], step[1])
                    time.sleep(tiempo_espera)
                ## click en la tienda
                pyautogui.click(lugar[0][0], lugar[0][1])
            
    # Iniciar ruta aleatoriamente
    rand = random.choice([True, False])
    rand= True
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