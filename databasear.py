def databasear():
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
            cur.execute("INSERT INTO objetos VALUES (Null, ?, ?)", (row[0], row[1]))
        cur.close()
    con.commit()
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
            cur.execute("INSERT INTO item_price VALUES (Null, ?, ?)", (r[-2], r[-1]))
            con.commit()
        response = cur.execute("SELECT * FROM item_price")
        for x in response:
            print(x)
    con.commit()
    con.close()

