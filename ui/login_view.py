import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, servicio, al_iniciar_sesion):
        super().__init__(master)
        self.servicio = servicio
        self.al_iniciar_sesion = al_iniciar_sesion
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Iniciar Sesión", font=("Arial", 16, "bold")).pack(pady=15)

        tk.Label(self, text="Usuario:").pack(pady=2)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=2)
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack(pady=5)

        btn = tk.Button(self, text="Ingresar", command=self.validar_login, width=15, bg="#4CAF50", fg="white")
        btn.pack(pady=15)

    def validar_login(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()

        usuario = self.servicio.autenticar(user, pwd)
        if usuario:
            self.al_iniciar_sesion(usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
