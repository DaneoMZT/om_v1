import sqlite3

def crear():    #Crear base de datos
    conn = sqlite3.connect('BD_Opmv.db')
    conn.commit()
    conn.close()
    

def crear_tabla():  #Crear una tabla
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE if not exists Invet_Opmv (
        numero text,
        vehiculo text,
        año integer,
        valor integer
        )
""")
    conn.commit()
    conn.close()

def agregar(numero, vehiculo, año, valor):
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Invet_Opmv VALUES ('{numero}', '{vehiculo}', '{año}', '{valor}')")
    conn.commit()
    conn.close()

def agregar_varios(Motos_lista_inicial):
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    inst = f"INSERT INTO Invet_Opmv VALUES (?, ?, ?, ?)"
    cursor.executemany(inst, Motos_lista_inicial)
    conn.commit()
    conn.close()

def leer():
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    inst = 'SELECT * FROM Invet_Opmv'
    cursor.execute(inst)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

def filtrar():
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    inst = 'SELECT * FROM Invet_Opmv WHERE nombre like "KAWAS%"'
    cursor.execute(inst)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

def modificar():    #'UPDATE [tabla] SET [campo] = [cambio] WHERE [filtracion]'
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    inst = 'UPDATE Invet_Opmv SET vehiculo = INDIA WHERE = "NINJA"'
    cursor.execute(inst)
    conn.commit()
    conn.close()

#def eliminar(vehiculo):
#    conn = sqlite3.connect('BD_Opmv.db')
#    cursor = conn.cursor()
#    inst = f'DELETE FROM Invet_Opmv WHERE vehiculo = "{}"'
#    cursor.execute(inst)
#    conn.commit()
#    conn.close()

def ordenar():
    conn = sqlite3.connect('BD_Opmv.db')
    cursor = conn.cursor()
    inst = 'SELECT * FROM BD_Opmv1 ORDER BY año DESC'
    cursor.execute(inst)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

#def crear_nueva(Motos_lista_ofertas):
#    conn = sqlite3.connect('BD_Opmv.db')
#    cursor = conn.cursor()
#    cursor.execute(
#        """CREATE TABLE if not exists Invet_Opmv_Esp (
#       numero text,
#        vehiculo text,
#        año integer,
#        valor integer
#        )
#""")
#    inst = f'INSERT INTO Invet_Opmv_Esp VALUES (?, ?, ?, ?)'
#    cursor.executemany(inst, lista2)
#    conn.commit()
#    conn.close()

crear()
crear_tabla()
agregar(1, 'KAWASAKI-400CC-VERDE ESPECIAL',2023,126378.84)
agregar_varios([(2, 'KAWASAKI-400CC-NINJA-400',2023, 110010.62), 
       (3, 'KAWASAKI-812CC-MULE-PRO-FXT-EPS',2022, 322835.52), 
       (4, 'KAWASAKI- 993CC-MULE-PRO-DTX-EPS',2022, 330743.14 ),
       (5, 'KAWASAKI-KLX-110R-L',2022, 44074.10 ),
       (6, 'KLX300SM',2023, 132024.39 ),
       (7, 'KAWASAKI-1000CC',2023, 293329.88 ),
       (8, 'TERYX KRX41000',2023, 595967.40 ),
       (9, 'KAWASAKI-783CC-TERYX4-MAX',2022, 366103.50 ),
       (10,'KAWASAKI-783CC-TERYX4 S-LE',2022, 366103.50),
       (11,'KAWASAKI- 783CC-TERYX-SPORT',2022, 366103.50),
       (12,'KAWASAKI-900CC',2023, 172047.14), 
       (13,'NINJA-ZX-10R',2023, 282619.90 )])
leer()
#filtrar()
#modificar()
#eliminar('NINJA')
#ordenar()
#crear_nueva([()])