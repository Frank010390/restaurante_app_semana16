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
        tab_productos = ttk.Frame(notebook)
        notebook.add(tab_productos, text="Productos")
        self.construir_tab_productos(tab_productos)

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
            # ====== SEMANA 14: PESTAÑA DE PRODUCTOS ======
    def construir_tab_productos(self, frame):
        # Contenedor: Formulario
        marco_form = ttk.LabelFrame(frame, text="Datos del Producto")
        marco_form.pack(fill="x", padx=15, pady=8)

        ttk.Label(marco_form, text="ID:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.ent_id_producto = ttk.Entry(marco_form, width=18)
        self.ent_id_producto.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(marco_form, text="Nombre:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.ent_nombre_prod = ttk.Entry(marco_form, width=30)
        self.ent_nombre_prod.grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(marco_form, text="Precio:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.ent_precio_prod = ttk.Entry(marco_form, width=18)
        self.ent_precio_prod.grid(row=1, column=1, padx=8, pady=8)

        # Contenedor: Botones
        marco_botones = ttk.LabelFrame(frame, text="Acciones")
        marco_botones.pack(fill="x", padx=15, pady=8)

        ttk.Button(marco_botones, text="✅ Registrar", command=self.registrar_producto).pack(side="left", padx=6, pady=6)
        ttk.Button(marco_botones, text="🔍 Cargar", command=self.cargar_producto).pack(side="left", padx=6, pady=6)
        ttk.Button(marco_botones, text="🔄 Actualizar", command=self.actualizar_producto).pack(side="left", padx=6, pady=6)
        ttk.Button(marco_botones, text="🗑️ Eliminar", command=self.eliminar_producto).pack(side="left", padx=6, pady=6)
        ttk.Button(marco_botones, text="🧹 Limpiar", command=self.limpiar_formulario_prod).pack(side="right", padx=6, pady=6)

        # Contenedor: Tabla
        marco_lista = ttk.LabelFrame(frame, text="Lista de Productos")
        marco_lista.pack(fill="both", expand=True, padx=15, pady=8)

        columnas = ("id", "nombre", "precio")
        self.tree_prod = ttk.Treeview(marco_lista, columns=columnas, show="headings", height=6)
        self.tree_prod.heading("id", text="ID")
        self.tree_prod.heading("nombre", text="Nombre")
        self.tree_prod.heading("precio", text="Precio")
        self.tree_prod.column("id", width=100)
        self.tree_prod.column("nombre", width=300)
        self.tree_prod.column("precio", width=120)
        self.tree_prod.pack(fill="both", expand=True, padx=5, pady=5)

        self.etq_msg_prod = ttk.Label(frame, text="✅ Listo", foreground="green")
        self.etq_msg_prod.pack(fill="x", padx=15, pady=2)

        self.refrescar_tabla_prod()

    def _leer_form_prod(self):
        try:
            id_p = self.ent_id_producto.get().strip()
            nombre = self.ent_nombre_prod.get().strip()
            precio = float(self.ent_precio_prod.get().strip())
            return {"id": id_p, "nombre": nombre, "precio": precio} if id_p and nombre and precio > 0 else None
        except:
            return None

    def limpiar_formulario_prod(self):
        self.ent_id_producto.delete(0, "end")
        self.ent_nombre_prod.delete(0, "end")
        self.ent_precio_prod.delete(0, "end")

    def refrescar_tabla_prod(self):
        for f in self.tree_prod.get_children():
            self.tree_prod.delete(f)
        for p in self.servicio.listar_productos():
            self.tree_prod.insert("", "end", values=(p["id"], p["nombre"], p["precio"]))

    def registrar_producto(self):
        d = self._leer_form_prod()
        if not d:
            self.etq_msg_prod.config(text="⚠️ Datos incompletos", foreground="orange")
            return
        if self.servicio.registrar_producto(d["id"], d["nombre"], d["precio"]):
            self.etq_msg_prod.config(text="✅ Registrado", foreground="green")
            self.limpiar_formulario_prod()
            self.refrescar_tabla_prod()
        else:
            self.etq_msg_prod.config(text="❌ No se pudo registrar", foreground="red")

    def cargar_producto(self):
        id_p = self.ent_id_producto.get().strip()
        p = self.servicio.buscar_producto(id_p)
        if p:
            self.ent_nombre_prod.delete(0, "end")
            self.ent_nombre_prod.insert(0, p["nombre"])
            self.ent_precio_prod.delete(0, "end")
            self.ent_precio_prod.insert(0, str(p["precio"]))
            self.etq_msg_prod.config(text="✅ Cargado", foreground="green")
        else:
            self.etq_msg_prod.config(text="❌ No encontrado", foreground="red")

    def actualizar_producto(self):
        d = self._leer_form_prod()
        if not d:
            self.etq_msg_prod.config(text="⚠️ Completa todos los datos", foreground="orange")
            return
        if self.servicio.actualizar_producto(d["id"], d["nombre"], d["precio"]):
            self.etq_msg_prod.config(text="✅ Actualizado", foreground="green")
            self.limpiar_formulario_prod()
            self.refrescar_tabla_prod()
        else:
            self.etq_msg_prod.config(text="❌ No se pudo actualizar", foreground="red")

    def eliminar_producto(self):
        id_p = self.ent_id_producto.get().strip()
        if self.servicio.eliminar_producto(id_p):
            self.etq_msg_prod.config(text="✅ Eliminado", foreground="green")
            self.limpiar_formulario_prod()
            self.refrescar_tabla_prod()
        else:
            self.etq_msg_prod.config(text="❌ No se pudo eliminar", foreground="red")

     