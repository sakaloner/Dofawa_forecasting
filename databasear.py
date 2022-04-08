'''
Sucede que hay que cambiar el codigo para que solo se ponga en la tabla
de objetos los objetos nuevos???, pero despues, por ahora es suficiente
con que se corra solamente la primera lo de popular la tbala de info_objetos
y que cada dia se updatee price_history.
Tambien hay que limpiar los objetos para que no se metan en la database
cosas vacias o erroneas
'''

def databasear():
    import os
    import sqlite3, csv
    ## error aveces de que no se hace el segundo for de insert
    from sqlite3 import Error

    def sql_connection():
        try:
            con = sqlite3.connect('dofawa.db')
            return con

        except Error:
            print(Error)

    def sql_table(con):
        cursorObj = con.cursor()
        cursorObj.execute('PRAGMA foreign_keys = ON')
        con.commit()

    con = sql_connection()

    #sql_table(con)
    '''
    # Creacion de la tabla de objetos inicial
    with con:
        cur = con.cursor()
        file = open("objetos.csv")
        rows = csv.reader(file)

        cuenta = 0
        ## poner en la tabla de objetos
        for row in rows:
            if cuenta == 0:
                cuenta += 1  
                continue
            cur.execute("INSERT INTO info_objetos VALUES (Null, ?, ?)", (row[0], row[1]))
        cur.close()
    con.commit()
    '''
    # Poner en la tabla del item_price
    with con:
        cur = con.cursor()
        file = open("objetos.csv")
        rows = csv.reader(file)
        cuenta = 0
        for r in rows:
            if cuenta == 0:
                cuenta += 1  
                continue
            cur.execute("INSERT INTO price_history VALUES (Null, ?, ?, ?)", (r[-2], r[-4] ,r[-1]))
            con.commit()
        response = cur.execute("SELECT * FROM price_history LIMIT 100")
        for x in response:
            print(x)
    con.commit()
    con.close()
    print('done')




