import tkinter as tk
from tkinter import ttk, messagebox

class LoginView:
    def __init__(self, root, servicio, callback_ingresar):
        self.root = root
        self.servicio = servicio
        self.callback_ingresar = callback_ingresar

        self.root.title("🔐 Iniciar Sesión")
        self.root.geometry("400x300")

        marco = ttk.Frame(root, padding=30)
        marco.pack(fill="both", expand=True)

        ttk.Label(marco, text="Usuario:", font=("Arial", 11)).pack(pady=5, anchor="w")
        self.entry_usuario = ttk.Entry(marco, width=35)
        self.entry_usuario.pack(pady=5)

        ttk.Label(marco, text="Contraseña:", font=("Arial", 11)).pack(pady=10, anchor="w")
        self.entry_clave = ttk.Entry(marco, width=35, show="*")
        self.entry_clave.pack(pady=5)

        ttk.Button(marco, text="Ingresar", command=self._validar_login).pack(pady=20)

    def _validar_login(self):
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_clave.get().strip()

        if self.servicio.validar_usuario(usuario, clave):
            self.callback_ingresar(usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")