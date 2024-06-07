from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button, DataTable, Input
from textual.containers import Horizontal
from coleccionproductos import ColeccionProductos

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Horizontal(
            Button("Añadir producto", id="btn_anadir_producto"),
            Button("Eliminar producto", id="btn_eliminar_producto")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_anadir_producto":
            self.app.switch_to_edit(action="add")
        elif event.button.id == "btn_eliminar_producto":
            self.app.switch_to_edit(action="delete")

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        table.clear()  # Clear existing rows

        if not table.columns:
            table.add_columns("ID", "Nombre del producto")

        # Load data from database
        productos = self.app.coleccion.leer()
        table.add_rows([(str(producto[0]), producto[1]) for producto in productos]) 

class EditScreen(Screen):
    def __init__(self, action="add", **kwargs):
        super().__init__(**kwargs)
        self.action = action

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="input_producto")
        yield Horizontal(
            Button("Aceptar", id="btn_aceptar"),
            Button("Cancelar", id="btn_cancelar")
        )
        yield Button("Volver", id="btn_volver")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        input_producto = self.query_one(Input).value
        if event.button.id == "btn_aceptar" and input_producto:
            if self.action == "add":
                self.app.coleccion.insertar(input_producto)
            elif self.action == "delete":
                self.app.coleccion.borrar(input_producto)
            self.app.switch_to_main()
        elif event.button.id == "btn_cancelar" or event.button.id == "btn_volver":
            self.app.switch_to_main()

class ModesApp(App):
    BINDINGS = [
        ("m", "switch_to_main", "Principal"),
        ("e", "switch_to_edit", "Edición"),
    ]
    def __init__(self):
        super().__init__()
        self.coleccion = ColeccionProductos()

    def on_mount(self) -> None:
        self.switch_to_main()

    def switch_to_main(self) -> None:
        self.push_screen(MainScreen())

    def switch_to_edit(self, action="add") -> None:
        self.action = action
        self.push_screen(EditScreen(action=action))

if __name__ == "__main__":
    app = ModesApp()
    app.run()
