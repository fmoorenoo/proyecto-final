from db import Db

SQLMDLCREATE_producto = '''
    CREATE TABLE IF NOT EXISTS producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL
    );
'''
SQLMDLCREATE_tienda = '''
    CREATE TABLE IF NOT EXISTS tienda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ubicacion TEXT NOT NULL
    );
'''
SQLMDLCREATE_trabajador = '''
    CREATE TABLE IF NOT EXISTS trabajador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_trabajador TEXT NOT NULL
    );
'''


ver_productos = '''SELECT * FROM producto'''
ver_trabajadores = '''SELECT * FROM trabajador'''
ver_tienda = '''SELECT * FROM tienda'''


insertar_producto = '''INSERT INTO producto (nombre_producto) VALUES '''
insertar_trabajador = '''INSERT INTO trabajador (nombre_trabajador) VALUES '''  
insertar_tienda = '''INSERT INTO tienda (ubicacion) VALUES '''           


SQLDDLUPDATEPART1 = '''UPDATE producto SET nombre_producto = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


borrar_producto = '''DELETE FROM producto WHERE id = '''
borrar_trabajador = '''DELETE FROM trabajador WHERE id = '''
borrar_tienda = '''DELETE FROM tienda WHERE id = '''


buscar_producto = '''SELECT id FROM producto WHERE nombre_producto LIKE '''
buscar_trabajador = '''SELECT id FROM trabajador WHERE nombre_trabajador LIKE '''
buscar_tienda = '''SELECT id FROM tienda WHERE ubicacion LIKE '''



class ColeccionTienda:
    DBNAME = 'tienda.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        
        self.con.execute(SQLMDLCREATE_producto)
        self.con.execute(SQLMDLCREATE_tienda)
        self.con.execute(SQLMDLCREATE_trabajador)

    def leer(self, tipo):
        if tipo == "pro":
            return self.con.execute(ver_productos).fetchall()
        elif tipo == "tra":
            return self.con.execute(ver_trabajadores).fetchall()
        elif tipo == "tnd":
            return self.con.execute(ver_tienda).fetchall()
        
    
    def insertar(self, nombre, tipo):
        if self.buscar(nombre, tipo) == 0:
            elstr = "('" + str(nombre) + "')"
            if tipo == "pro":
                self.con.execute(insertar_producto + elstr)
            elif tipo == "tra":
                self.con.execute(insertar_trabajador + elstr)
            elif tipo == "tnd":
                self.con.execute(insertar_tienda + elstr)

            self.con.commit()


    def borrar(self, nombre, tipo):
        id = self.buscar(nombre, tipo) 
        if id != 0:
            if tipo == "pro":
                self.con.execute(borrar_producto + str(id))
            elif tipo == "tra":
                self.con.execute(borrar_trabajador + str(id))
            elif tipo == "tnd":
                self.con.execute(borrar_tienda + str(id))

            self.con.commit()


    def buscar(self, nombre, tipo):
        resultado = 0
        elstr = '"' + str(nombre) + '"'
        if tipo == "pro":
            res = self.con.execute(buscar_producto + elstr)
        elif tipo == "tra":
            res = self.con.execute(buscar_trabajador + elstr)
        elif tipo == "tnd":
            res = self.con.execute(buscar_tienda + elstr)
            
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]
        return resultado 