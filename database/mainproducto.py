from coleccionproductos import ColeccionProductos
from producto import Producto

cc = ColeccionProductos()

# cc.actualizar()
cc.borrar(Producto('Destornillador'))



# print(cc.buscar(Producto()))


print(cc.leer())