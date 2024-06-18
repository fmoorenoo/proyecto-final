from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Button, Input
from textual.containers import Horizontal, Vertical

class AñadirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del producto", id="producto")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
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



class ConstruirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Ubicación de la nueva tienda", id="tienda")
        yield Horizontal(
            Button("Construir", id="boton_aceptar"),
            Button("Nah, muchos gastos", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        ubi = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and ubi:
            self.app.coleccion.insertar(ubi, "tnd")
            self.app.switch_to_tiendas()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_tiendas()





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
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        producto = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and producto:
            self.app.coleccion.borrar(producto, "pro")
            self.app.switch_to_main()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_main()


class DestruirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Ubicación de la tienda que desea destruir", id="tienda")
        yield Horizontal(
            Button("Destruir", id="boton_aceptar"),
            Button("Mejor no", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        ubi = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and ubi:
            self.app.coleccion.borrar(ubi, "tnd")
            self.app.switch_to_tiendas()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_tiendas()