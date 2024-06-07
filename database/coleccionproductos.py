from db import Db
from producto import Producto

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


SQLDDLSELECT = '''
    SELECT * FROM producto
'''

SQLDDLINSERT = '''INSERT INTO producto (nombre_producto) VALUES '''
                #Hay que concatenar

SQLDDLUPDATEPART1 = '''UPDATE producto SET nombre_producto = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM producto WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM producto WHERE nombre_producto LIKE '''
                #Hay que concatenar


class ColeccionProductos:
    DBNAME = 'tienda.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        
        self.con.execute(SQLMDLCREATE_producto)
        self.con.execute(SQLMDLCREATE_tienda)
        self.con.execute(SQLMDLCREATE_trabajador)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, nombre_producto) -> None:
        if self.buscar(nombre_producto) == 0:
            elstr = "('" + str(nombre_producto) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, producto:str, nuevoProducto:str):
        id = self.buscar(producto)
        if id != 0:
            elstr = SQLDDLUPDATEPART1 + nuevoProducto 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, nombre_producto):
        id = self.buscar(nombre_producto) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, nombre_producto:Producto) -> int:
        resultado = 0
        elstr = '"' + str(nombre_producto) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]
        return resultado