
def reading_im():
    from PIL import Image
    import pytesseract, time, re, os, cv2, csv
    from icecream import ic
    import numpy as np
    import datetime, time
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #2. OpenCV lee las imagenes que descargue para ver el precio

    ##### preprocesing ######
    # quitar tildes
    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),)
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

    # preprocesamiento
    def clean(txt):
        x = re.sub("[^\w|\.|\t]", " ", txt)
        x = x.strip()
        return (normalize(x))

    # lista de archivos para enviar al for
    fecha = time.gmtime()
    nombre_carpeta = f'objetos-{fecha.tm_mday}_{fecha.tm_mon}_{fecha.tm_year}'
    lista = os.listdir(f'{nombre_carpeta}')
    conta = 0

    # sortear los files
    def num_sort(test_string):
        return list(map(int, re.findall(r'\d+', test_string)))[0]
    lista = sorted(lista, key=num_sort)

    '''
    # Test shit
    # abrir la imagen con cv2
    img = cv2.imread("objetos/2.png")
    # cambiarla a blanco y negro
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # volverlo un acrhivo de PIL
    t = Image.fromarray(np.uint8(grayImage*255))
    #c crop
    t = t.crop((480,0,525,43))
    t.show()
    # leerlo
    p = pytesseract.image_to_string(t)
    print(p)
    '''
    # open the file in the write mode
    with open('objetos.csv', 'w', newline='') as f:
        # crear writer object
        writer = csv.writer(f)
        writer.writerow(['nombre', 'categoria', 'precio', 'datetime'])
        # go trough every image and analize it
        for i, file in enumerate(lista):
            print(f"num:{i}")
            # pal csv
            lista_csv = []
            # abrir la imagen con cv2
            img = cv2.imread(f"{nombre_carpeta}\{file}")
            # cambiarla a blanco y negro
            ima = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # volverlo un acrhivo de PIL
            im = Image.fromarray(np.uint8(ima*255))

            im_name = im.crop((40,0,250,43))
            name = clean(pytesseract.image_to_string(im_name, lang='spa'))
            #im_name.show()
            ic(name)
            lista_csv.append(name)

            im_cat = im.crop((250,0,370,43))
            categoria = clean(pytesseract.image_to_string(im_cat, lang='spa'))
            #print(categoria)
            #im_cat.show()
            ic(categoria)
            lista_csv.append(categoria)


            im_price = im.crop((430,0,525,43))
            price = clean(pytesseract.image_to_string(im_price))
            price = ''.join(price.split())
            ic(price)
            #print(int(price))
            #im_price.show()
            lista_csv.append(price)
            ic(lista_csv)
            ### la hora
            fecha = datetime.datetime.now()
            fecha_str = fecha.strftime(r'%Y/%m/%d %H:%M:%S')
            lista_csv.append(fecha_str) 
            ## contar los nombres incompletos
            if '...' in name:
                conta += 1
            ## guardar en el csv
            ## guardar la hora
            writer = csv.writer(f)
            writer.writerow(lista_csv)


    print('Done')
    print(f'# nombres incompletos: {conta}')

    ### Poner los datos en un archivo csv
