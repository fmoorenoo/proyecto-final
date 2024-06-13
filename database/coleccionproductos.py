from db import Db

SQLMDLCREATE_producto = '''
    CREATE TABLE IF NOT EXISTS producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL
    );
'''
SQLMDLCREATE_tienda = '''
    CREATE TABLE IF NOT EXISTS tienda (
        ubicacion TEXT NOT NULL,
        precio INTEGER NOT NULL
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


insertar_producto = '''INSERT INTO producto (nombre_producto) VALUES '''
insertar_trabajador = '''INSERT INTO trabajador (nombre_trabajador) VALUES '''            


SQLDDLUPDATEPART1 = '''UPDATE producto SET nombre_producto = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


borrar_producto = '''DELETE FROM producto WHERE id = '''
borrar_trabajador = '''DELETE FROM trabajador WHERE id = '''


buscar_producto = '''SELECT id FROM producto WHERE nombre_producto LIKE '''
buscar_trabajador = '''SELECT id FROM trabajador WHERE nombre_trabajador LIKE '''



class ColeccionProductos:
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
        
    
    def insertar(self, nombre, tipo):
        if self.buscar(nombre, tipo) == 0:
            elstr = "('" + str(nombre) + "')"
            if tipo == "pro":
                self.con.execute(insertar_producto + elstr)
            elif tipo == "tra":
                self.con.execute(insertar_trabajador + elstr)
            self.con.commit()

    def actualizar(self, producto, nuevoProducto):
        id = self.buscar(producto)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + nuevoProducto 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)
            self.con.commit()

    def borrar(self, nombre, tipo):
        id = self.buscar(nombre, tipo) 
        if id != 0:
            if tipo == "pro":
                self.con.execute(borrar_producto + str(id))
            elif tipo == "tra":
                self.con.execute(borrar_trabajador + str(id))
            self.con.commit()

    def buscar(self, nombre, tipo):
        resultado = 0
        elstr = '"' + str(nombre) + '"'
        if tipo == "pro":
            res = self.con.execute(buscar_producto + elstr)
        elif tipo == "tra":
            res = self.con.execute(buscar_trabajador + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]
        return resultado 