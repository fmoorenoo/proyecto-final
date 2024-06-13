from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button, DataTable, Label
from textual.containers import Horizontal, Vertical


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("PRODUCTOS DE LA TIENDA")
        yield Horizontal(
            DataTable(classes="table"),
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
            DataTable(classes="table"),
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