import sqlite3
from sqlite3 import Error
    #Creamos la conexion con la base de datos ventas

con=sqlite3.connect('almacenventas2.db')
cursor=con.cursor()
#Crea la base de datos de sqlite almacenventas.db
def crearTablas():
    con=sqlite3.connect('almacenventas2.db')
    cursor=con.cursor()
    sql="""CREATE TABLE IF NOT EXISTS "ALMACEN" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"ARTICULO"	TEXT NOT NULL,
	"PRECIO"	REAL NOT NULL,
    "CANTIDAD"	INTEGER NOT NULL	
    )"""
    cursor.execute(sql)
    sql="""CREATE TABLE IF NOT EXISTS "TRABAJADOR" (
	"NUMEMPLEADO"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"NOMBRE"	TEXT NOT NULL		
    )"""
    cursor.execute(sql)
    
#forma 1 de insertar un articulo  
def insertaArticulo():       
    print("Vas a crear un articulo nuevo")
    num = int(input("Escribe la ID\n"))
    articulo=input("Escribe el nombre del ARTICULO\n")
    precio=int(input("Escribe el PRECIO del ARTICULO\n"))
    cant = int(input("Escribe la CANTIDAD\n"))
    sql=f"INSERT INTO ALMACEN VALUES ({num},'{articulo}',{precio},{cant})"   
    cursor.execute(sql)    
def insertaTrabajador():
    print("Vas a crear un nuevo trabajador")
    num = int(input("Escribe el NUMERO delTRABAJADOR\n"))
    nombre=input("Escribe el nombre del TRABAJADOR\n")
    sql=f"INSERT INTO TRABAJADOR VALUES ({num},'{nombre}')"   
    cursor.execute(sql)  


#forma 2 de insertar un articulo  
def insertaBaseArticulo2(inserta):    
    print("Vas a crear un articulo nuevo")
    cursor.execute('INSERT INTO ALMACEN(ID,ARTICULO,PRECIO,CANTIDAD) VALUES(?, ?, ?, ?)', inserta)
    
#actualizar la base de datos
def actualizaPrecioBD():
    
    articulo=input("Escribe el nombre del ARTICULO al que le quieras cambiar el precio\n")
    precio=int(input("Escribe el PRECIO que quieres que tenga ahora\n"))
    sql=f'UPDATE ALMACEN SET PRECIO = {precio} where ARTICULO = "{articulo}"'    
    cursor.execute(sql)
def venderProducto():
    
    articulo=input("Escribe el nombre del ARTICULO que vas a vender\n")
    cant=int(input("Escribe el PRECIO que quieres que tenga ahora\n"))
    sql=f'UPDATE ALMACEN SET CANTIDAD =1 {cant} where ARTICULO = "{articulo}"'    
    cursor.execute(sql)
#actualizar la base de datos
def actualizaCantidadArticulosBD():
    
    articulo=input("Escribe el nombre del ARTICULO que vas a vender\n")
    cantidad=int(input("Escribe la cantidad que quieres vender\n"))

    sql=f'UPDATE ALMACEN SET CANTIDAD = {cantidad} where ARTICULO = "{articulo}"'    
    print(f'Cantidad articulos vendidos {cantidad}  ')
    cursor.execute(sql)

#forma 1 de hacer una sentencia
def crearSentencia():

    cursor.execute('SELECT * FROM ALMACEN')
    
    [print(linea) for linea in cursor.fetchall()]
    sentencia = cursor.fetchall()
    for linea in sentencia:
        print(linea)

#forma 2 de hacer una sentencia
def crearSentencia2():

    cursor.execute('SELECT * FROM ALMACEN')
    print("\nMuestrame todo lo que hay en el almacen\n")
    [print(linea) for linea in cursor.fetchall()]
    cursor.execute('SELECT ID, ARTICULO FROM ALMACEN WHERE PRECIO < 30')
    print("\nMuestrame los articulos que valen menos de 30 euros\n")
    [print(linea) for linea in cursor.fetchall()]
    cursor.execute('SELECT SUM(PRECIO) FROM ALMACEN')
    print("\nMuestrame el valor de todo el almacen\n")
    [print(linea) for linea in cursor.fetchall()]
    print(" Euros")
#borrar la base de datos entera
def borrarTodalaBBDD():
    
    cursor.execute('DELETE * FROM TRABAJADOR')
#eliminar una tabla
def eliminarTabla():
    cursor.execute('DROP table if exists TRABAJADOR')
def reponer():
    
    id_reponer=input("Escribe el ID del ARTICULO que quieres reponer\n")
    cantidad=int(input("Escribe la cantidad que entra\n"))

    sqlr1=f"SELECT CANTIDAD FROM ALMACEN WHERE ID = {id_reponer}"
    cursor.execute(sqlr1)
    linea = cursor.fetchall()
    cant = int(linea[0][0])
    cantres = cant + cantidad

    sqlr2=f'UPDATE ALMACEN SET CANTIDAD = {cantres} where ID = {id_reponer}'    
    cursor.execute(sqlr2)

def vender():
    
    id_Vender=input("Escribe el ID del ARTICULO que quieres vender\n")
    cantidad=int(input("Escribe la cantidad que Vendes\n"))
    
    sqlv1=f"SELECT CANTIDAD FROM ALMACEN WHERE ID = {id_Vender}"
    cursor.execute(sqlv1)
    linea = cursor.fetchall()
    cant = int(linea[0][0])
    cantres = cant - cantidad
    sqlv2=f'UPDATE ALMACEN SET CANTIDAD = {cantres} where ID = {id_Vender}'    
    cursor.execute(sqlv2)

crearTablas()   #CREA LAS TABLAS SI NO EXISTEN  Y ME CONECTO A LA BBDD



while True:
    con=sqlite3.connect('almacenventas2.db')
    cursor=con.cursor()
    try:

        print("""

        Menú

        [1] Vender producto

        [2] Añadir cantidad de producto

        [3] Nuevo Articulo

        [4] Ver el inventario

        [5] Salir

        """)

        opcion = int(input("¿Qué deseas hacer?: "))

    except ValueError:

        print("Favor de ingresar una opción válida")

    else:

        if opcion < 1 or opcion > 5:

            print("{} no es una opción válida".format(opcion) )

            continue

        if opcion == 1:
                    
            try:
                vender()  
                
            except Error:               #SI SALTA UNA EXCEPCION LA CAPTURO Y CONTINUO
                print(Error)
                print("La id ya existe y no se puede repetir")
                con=sqlite3.connect('almacen.db')
                cursor=con.cursor()
            finally:                    #LO EJECUTA SIEMPRE
                con.commit()  
        elif opcion == 2:
             #modifica la cantidad de piezas de un articulo
            try:
                reponer()#METO UN ARTICULO EN EL ALMACEN
                
            except Error:               #SI SALTA UNA EXCEPCION LA CAPTURO Y CONTINUO
                print(Error)
                print("La id ya existe y no se puede repetir")
                con=sqlite3.connect('almacen.db')
                cursor=con.cursor()
            finally:                    #LO EJECUTA SIEMPRE
                con.commit()  
                    
        elif opcion == 3:
             #modifica la cantidad de piezas de un articulo
            try:
                
                  
                addArticulos=int(input("¿Cuantos articulos quieres introducir?\n"))
                for i in range(addArticulos):
                    insertaArticulo()      #METO UN ARTICULO EN EL ALMACEN
                
            except Error:               #SI SALTA UNA EXCEPCION LA CAPTURO Y CONTINUO
                print(Error)
                print("La id ya existe y no se puede repetir")
                con=sqlite3.connect('almacen.db')
                cursor=con.cursor()
            finally:                    #LO EJECUTA SIEMPRE
                con.commit()  
            
        elif opcion == 4:
            print("\nVas a ver el inventario\n")
            crearSentencia() # ver el inventario
            

        else:
             
            break
      #SIN ESTA FUNCION NO MANDA LOS DATOS A LA BBDD

print("Gracias por su compra")   
    





try:
    
    #eliminarTabla()       #ELIMINA LA TABLA TRABAJADOR
          #CREO LAS SENTENCIAS PARA VER LA BASE DE DATOS
    #for i in range(5):         #CON UN FORI METO VARIOS ARTICULOS
    #   insertaArticulo()      #METO UN ARTICULO EN EL ALMACEN
    #insertaTrabajador()    #CREO UN TRABAJADOR
    
    inserta=(17,'TORNILLO DEL 5',5,12)  #METO ARTICULO FORMA 2
    insertaBaseArticulo2(inserta)
    
except Error:               #SI SALTA UNA EXCEPCION LA CAPTURO Y CONTINUO
    print(Error)
    print("La id ya existe y no se puede repetir")
    con=sqlite3.connect('almacenventas.db')
    cursor=con.cursor()
finally:                    #LO EJECUTA SIEMPRE
    
    con.commit()            #SIN ESTA FUNCION NO MANDA LOS DATOS A LA BBDD
    con.close()             #CIERRA LA CONEXION