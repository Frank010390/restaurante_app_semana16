import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, master, servicio, usuario, al_cerrar_sesion):
        super().__init__(master)
        self.servicio = servicio
        self.usuario = usuario
        self.al_cerrar_sesion = al_cerrar_sesion
        self.crear_widgets()

    def crear_widgets(self):
        panel_top = tk.Frame(self, bg="#333333")
        panel_top.pack(fill="x")

        lbl_info = f"Bienvenido: {self.usuario['username']} ({self.usuario['rol']})"
        tk.Label(panel_top, text=lbl_info, fg="white", bg="#333333", font=("Arial", 10, "bold")).pack(side="left", padx=10, pady=8)

        btn_salir = tk.Button(panel_top, text="Cerrar Sesión", command=self.al_cerrar_sesion, bg="#f44336", fg="white")
        btn_salir.pack(side="right", padx=10, pady=5)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        tab_usuarios = ttk.Frame(notebook)
        notebook.add(tab_usuarios, text="Usuarios")
        self.construir_tab_usuarios(tab_usuarios)

        tab_ventas = ttk.Frame(notebook)
        notebook.add(tab_ventas, text="Ventas")
        self.mostrar_ventas_pendiente(tab_ventas)

    def construir_tab_usuarios(self, frame):
        columnas = ("username", "rol")
        tree = ttk.Treeview(frame, columns=columnas, show="headings")
        tree.heading("username", text="Usuario")
        tree.heading("rol", text="Rol")
        
        tree.column("username", width=150)
        tree.column("rol", width=150)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            tree.insert("", "end", values=(u["username"], u["rol"]))

        tree.pack(fill="both", expand=True, padx=5, pady=5)

    def mostrar_ventas_pendiente(self, frame):
        lbl = tk.Label(frame, text="La funcionalidad 'Ventas' está en desarrollo.", font=("Arial", 11))
        lbl.pack(pady=30)

     