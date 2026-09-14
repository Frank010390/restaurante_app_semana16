import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AppRestaurante:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("520x380")
        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()
        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = LoginView(self.root, self.servicio, self.al_iniciar_sesion)
        self.vista_actual.pack(fill="both", expand=True)

    def al_iniciar_sesion(self, usuario):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = MainView(self.root, self.servicio, usuario, self.cerrar_sesion)
        self.vista_actual.pack(fill="both", expand=True)

    def cerrar_sesion(self):
        self.mostrar_login()

if __name__ == "__main__":
    print("Iniciando aplicacion")
    root = tk.Tk()
    app = AppRestaurante(root)
    root.mainloop()