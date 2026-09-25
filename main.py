import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AppRestaurante:
    def __init__(self, root):
        self.root = root
        self.servicio = RestauranteServicio()
        self.ventana_actual = None
        self._iniciar_login()

    def _iniciar_login(self):
        # No destruimos root, solo limpiamos contenido anterior
        for widget in self.root.winfo_children():
            widget.destroy()
        self.ventana_actual = LoginView(self.root, self.servicio, self._ingresar)

    def _ingresar(self, nombre_usuario):
        # Borramos contenido anterior ANTES de crear el nuevo
        for widget in self.root.winfo_children():
            widget.destroy()
        self.ventana_actual = MainView(self.root, self.servicio, nombre_usuario, self._iniciar_login)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = AppRestaurante(raiz)
    raiz.mainloop()