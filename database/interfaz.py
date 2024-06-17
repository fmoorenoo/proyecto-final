from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Button, DataTable, Label
from textual.containers import Horizontal, Vertical
from coleccionTienda import ColeccionTienda
from pantallas import AñadirScreen, DeleteScreen, ContratarScreen, DespedirScreen, ConstruirScreen, DestruirScreen


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("PRODUCTOS DE LA TIENDA")
        yield Horizontal(
            DataTable(classes="table1"),
            Vertical(
                Button("Añadir producto", id="boton_anadirP"),
                Button("Eliminar producto", id="boton_eliminarP")
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirP":
            self.app.switch_to_edit("p")
        elif event.button.id == "boton_eliminarP":
            self.app.switch_to_delete("p")

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        table.clear()

        if not table.columns:
            table.add_columns("ID", "Nombre del producto")

        productos = self.app.coleccion.leer("pro")
        for producto in productos:
            table.add_rows([(str(producto[0]), producto[1])])



class TrabajadoresScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("TRABAJADORES DE LA TIENDA")
        yield Horizontal(
            DataTable(classes="table2"),
            Vertical(
                Button("Contratar Trabajador", id="boton_anadirT"),
                Button("Despedir Trabajador", id="boton_eliminarT")
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirT":
            self.app.switch_to_edit("t")
        elif event.button.id == "boton_eliminarT":
            self.app.switch_to_delete("t")

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        table.clear()

        if not table.columns:
            table.add_columns("ID", "Nombre del Trabajador")

        trabajadores = self.app.coleccion.leer("tra")
        for trabajador in trabajadores:
            table.add_rows([(str(trabajador[0]), trabajador[1])])



class TiendasScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("TODAS NUESTRAS TIENDAS")
        yield Horizontal(
            DataTable(classes="table3"),
            Vertical(
                Button("Construir tienda", id="boton_anadirTn"),
                Button("Destruir tienda", id="boton_eliminarTn")
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirTn":
            self.app.switch_to_edit("tnd")
        elif event.button.id == "boton_eliminarTn":
            self.app.switch_to_delete("tnd")

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "none"
        table.clear()

        if not table.columns:
            table.add_columns("ID", "Ubicaciones")

        tiendas = self.app.coleccion.leer("tnd")
        for tienda in tiendas:
            table.add_rows([(str(tienda[0]), tienda[1])])


class FooterApp(App):
    BINDINGS = [
        ("p", "switch_mode('main')", "Productos"),  
        ("t", "switch_mode('trabajadores')", "Trabajadores"),
        ("i", "switch_mode('tiendas')", "Ver tiendas"),
        ("c", "quit", "Cerrar Programa"),
    ]
    MODES = {
        "main": MainScreen,  
        "trabajadores": TrabajadoresScreen,
        "tiendas": TiendasScreen,
    }
    def compose(self) -> ComposeResult:
        yield Footer()


class Pantallas(FooterApp):
    CSS_PATH = "styles.tcss"

    def __init__(self):
        super().__init__()
        self.coleccion = ColeccionTienda()
    
    def on_mount(self) -> None:
        self.switch_to_main()

    def switch_to_main(self) -> None:
        self.push_screen(MainScreen())

    def switch_to_trabajadores(self) -> None:
        self.push_screen(TrabajadoresScreen())

    def switch_to_tiendas(self) -> None:
        self.push_screen(TiendasScreen())


    def switch_to_edit(self, tipo) -> None:
        if tipo == "t":
            self.push_screen(ContratarScreen())
        elif tipo == "p":
            self.push_screen(AñadirScreen())
        elif tipo == "tnd":
            self.push_screen(ConstruirScreen())

    def switch_to_delete(self, tipo) -> None:
        if tipo == "t":
            self.push_screen(DespedirScreen())
        elif tipo == "p":
            self.push_screen(DeleteScreen())
        elif tipo == "tnd":
            self.push_screen(DestruirScreen())
        


if __name__ == "__main__":
    app = Pantallas()
    app.run()