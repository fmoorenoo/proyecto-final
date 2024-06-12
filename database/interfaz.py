from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button, DataTable, Input
from textual.containers import Horizontal
from coleccionproductos import ColeccionProductos

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Horizontal(
            Button("Añadir producto", id="boton_anadir"),
            Button("Eliminar producto", id="boton_eliminar")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadir":
            self.app.switch_to_edit()

        elif event.button.id == "boton_eliminar":
            self.app.switch_to_delete()

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        table.clear()

        if not table.columns:
            table.add_columns("ID", "Nombre del producto")

        productos = self.app.coleccion.leer()
        for producto in productos:
            table.add_rows([(str(producto[0]), producto[1])]) 


class EditScreen(Screen):
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="input_producto")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Button("Volver", id="boton_volver")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        input_producto = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and input_producto:
            self.app.coleccion.insertar(input_producto)
            self.app.switch_to_main()

        elif event.button.id == "boton_cancelar" or event.button.id == "boton_volver":
            self.app.switch_to_main()


class DeleteScreen(Screen):
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="input_producto")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Button("Volver", id="boton_volver")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        producto = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and producto:
            self.app.coleccion.borrar(producto)
            self.app.switch_to_main()

        elif event.button.id == "boton_cancelar" or event.button.id == "boton_volver":
            self.app.switch_to_main()



class Pantallas(App):
    CSS_PATH = "styles.tcss"
    
    def __init__(self):
        super().__init__()
        self.coleccion = ColeccionProductos()
    
    def on_mount(self) -> None:
        self.switch_to_main()

    def switch_to_main(self) -> None:
        self.push_screen(MainScreen())

    def switch_to_edit(self) -> None:
        self.push_screen(EditScreen())

    def switch_to_delete(self) -> None:
        self.push_screen(DeleteScreen())


if __name__ == "__main__":
    app = Pantallas()
    app.run()