from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button, DataTable, Input
from textual.containers import Horizontal
from textual.binding import Binding
from coleccionproductos import ColeccionProductos
from pantallas import MainScreen, TrabajadoresScreen

class AñadirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="producto")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Button("Volver", id="boton_volver")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        producto = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and producto:
            self.app.coleccion.insertar(producto, "pro")
            self.app.switch_to_main()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_main()

class ContratarScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del nuevo trabajador", id="trabajador")
        yield Horizontal(
            Button("Contratar", id="boton_aceptar"),
            Button("Me arrepiento", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        trabajador = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and trabajador:
            self.app.coleccion.insertar(trabajador, "tra")
            self.app.switch_to_trabajadores()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_trabajadores()



class DespedirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del trabajador", id="trabajador")
        yield Horizontal(
            Button("Despedir", id="boton_aceptar"),
            Button("Perdonar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        trabajador = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and trabajador:
            self.app.coleccion.borrar(trabajador, "tra")
            self.app.switch_to_trabajadores()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_trabajadores()


class DeleteScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="producto")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Button("Volver", id="boton_volver")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        producto = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and producto:
            self.app.coleccion.borrar(producto, "pro")
            self.app.switch_to_main()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_main()


class FooterApp(App):
    BINDINGS = [
        ("p", "switch_mode('main')", "Productos"),  
        ("t", "switch_mode('trabajadores')", "Trabajadores"),
        ("c", "quit", "Cerrar Programa"),
    ]
    MODES = {
        "main": MainScreen,  
        "trabajadores": TrabajadoresScreen,
        
    }
    def compose(self) -> ComposeResult:
        yield Footer()


class Pantallas(FooterApp):
    CSS_PATH = "styles.tcss"

    def __init__(self):
        super().__init__()
        self.coleccion = ColeccionProductos()
    
    def on_mount(self) -> None:
        self.switch_to_main()

    def switch_to_main(self) -> None:
        self.push_screen(MainScreen())

    def switch_to_edit(self, tipo) -> None:
        if tipo == "t":
            self.push_screen(ContratarScreen())
        elif tipo == "p":
            self.push_screen(AñadirScreen())

    def switch_to_delete(self, tipo) -> None:
        if tipo == "t":
            self.push_screen(DespedirScreen())
        elif tipo == "p":
            self.push_screen(DeleteScreen())
        

    def switch_to_trabajadores(self) -> None:
        self.push_screen(TrabajadoresScreen())


if __name__ == "__main__":
    app = Pantallas()
    app.run()