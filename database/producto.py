class Producto:
    def __init__(self, producto:str) -> None:
        self.producto = producto

    def __str__(self) -> str:
        return self.producto
    
    def leer(self) -> str:
        return self.producto