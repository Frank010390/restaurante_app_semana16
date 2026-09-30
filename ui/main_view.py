import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, root, servicio, usuario_actual, callback_cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = callback_cerrar_sesion
        self.usuario_seleccionado = None

        self.root.title("🍽️ Gestión de Restaurante — Semana 16")
        self.root.geometry("950x650")

        # Cargar imágenes
        try:
            self.icono_app = tk.PhotoImage(file="assets/icons/icono.png")
            self.root.iconphoto(True, self.icono_app)
            self.logo_app = tk.PhotoImage(file="assets/logo/logo.png")
        except Exception as e:
            print(f"Imágenes no cargadas: {e}")

        # Cuaderno de pestañas
        self.cuaderno = ttk.Notebook(root)
        self.cuaderno.pack(pady=15, padx=15, fill="both", expand=True)

        # Crear marcos
        self.frame_usuarios = ttk.Frame(self.cuaderno)
        self.frame_productos = ttk.Frame(self.cuaderno)
        self.frame_ventas = ttk.Frame(self.cuaderno)

        # Verificar rol para mostrar pestaña
        datos_usuario = self.servicio.buscar_usuario(usuario_actual)
        es_admin = datos_usuario and datos_usuario.get("rol") == "Administrador"

        if es_admin:
            self.cuaderno.add(self.frame_usuarios, text="👥 Gestión de Usuarios")
        self.cuaderno.add(self.frame_productos, text="📦 Productos")
        self.cuaderno.add(self.frame_ventas, text="💰 Ventas")

        # Construir cada sección
        if es_admin:
            self._construir_usuarios()
        self._construir_productos()
        self._construir_ventas()

        # Botón cerrar sesión
        ttk.Button(root, text="Cerrar Sesión", command=self._salir).pack(pady=5)

    # ============================================================
    # GESTIÓN DE USUARIOS — CRUD + EVENTOS
    # ============================================================
    def _construir_usuarios(self):
        # Cabecera con logo
        marco_superior = ttk.Frame(self.frame_usuarios)
        marco_superior.pack(fill="x", pady=5)
        if hasattr(self, 'logo_app'):
            ttk.Label(marco_superior, image=self.logo_app).pack(side="left", padx=10)
        ttk.Label(marco_superior, text=f"Gestión de Usuarios — Bienvenido: {self.usuario_actual}",
                  font=("Arial", 12, "bold")).pack(side="left", padx=10)

        # Formulario
        marco_form = ttk.LabelFrame(self.frame_usuarios, text="Datos del Usuario")
        marco_form.pack(padx=15, pady=10, fill="x")

        ttk.Label(marco_form, text="Nombre de Usuario:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.entry_nombre_usu = ttk.Entry(marco_form)
        self.entry_nombre_usu.grid(row=0, column=1, padx=5, pady=8)

        ttk.Label(marco_form, text="Contraseña:").grid(row=0, column=2, padx=5, pady=8, sticky="w")
        self.entry_clave_usu = ttk.Entry(marco_form, show="*")
        self.entry_clave_usu.grid(row=0, column=3, padx=5, pady=8)

        ttk.Label(marco_form, text="Rol:").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.cmb_rol = ttk.Combobox(marco_form, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.cmb_rol.set("Empleado")
        self.cmb_rol.grid(row=1, column=1, padx=5, pady=8)

        # Botones con command=
        marco_botones = ttk.Frame(marco_form)
        marco_botones.grid(row=1, column=2, columnspan=2, padx=5, pady=8)

        self.btn_registrar = ttk.Button(marco_botones, text="✅ Registrar", command=self._registrar_usuario)
        self.btn_registrar.grid(row=0, column=0, padx=3)

        self.btn_actualizar = ttk.Button(marco_botones, text="🔄 Actualizar", command=self._actualizar_usuario, state="disabled")
        self.btn_actualizar.grid(row=0, column=1, padx=3)

        self.btn_eliminar = ttk.Button(marco_botones, text="🗑️ Eliminar", command=self._eliminar_usuario, state="disabled")
        self.btn_eliminar.grid(row=0, column=2, padx=3)

        self.btn_limpiar = ttk.Button(marco_botones, text="🧹 Limpiar", command=self._limpiar_formulario_usu)
        self.btn_limpiar.grid(row=0, column=3, padx=3)

        # Tabla de usuarios
        marco_tabla = ttk.LabelFrame(self.frame_usuarios, text="Usuarios Registrados")
        marco_tabla.pack(padx=15, pady=10, fill="both", expand=True)

        self.tabla_usu = ttk.Treeview(marco_tabla, columns=("nombre", "rol"), show="headings", height=8)
        self.tabla_usu.heading("nombre", text="Nombre de Usuario")
        self.tabla_usu.heading("rol", text="Rol")
        self.tabla_usu.column("nombre", width=300)
        self.tabla_usu.column("rol", width=200)
        self.tabla_usu.pack(fill="both", expand=True)

        # ============================================================
        # ✅ TODOS LOS EVENTOS — AQUÍ ESTÁN COMPLETOS
        # ============================================================
        # Clic en fila de la tabla
        self.tabla_usu.bind("<<TreeviewSelect>>", self._al_seleccionar_tabla_usu)
        
        # Tecla ENTER en campos de texto → registra
        self.entry_nombre_usu.bind("<Return>", self._al_presionar_enter)
        self.entry_clave_usu.bind("<Return>", self._al_presionar_enter)
        self.cmb_rol.bind("<Return>", self._al_presionar_enter)
        
        # Tecla ESCAPE → limpia TODO (en el marco y en cada campo)
        self.frame_usuarios.bind("<Escape>", self._al_presionar_escape)
        self.entry_nombre_usu.bind("<Escape>", self._al_presionar_escape)
        self.entry_clave_usu.bind("<Escape>", self._al_presionar_escape)
        self.cmb_rol.bind("<Escape>", self._al_presionar_escape)
        
        # Cambio de selección en el desplegable de Rol
        self.cmb_rol.bind("<<ComboboxSelected>>", self._al_cambiar_rol)

        self._actualizar_tabla_usuarios()

    # --- Callbacks de eventos ---
    def _al_seleccionar_tabla_usu(self, event):
        seleccion = self.tabla_usu.selection()
        if not seleccion:
            return
        fila = self.tabla_usu.item(seleccion[0])["values"]
        self.usuario_seleccionado = fila[0]
        self.entry_nombre_usu.delete(0, tk.END)
        self.entry_nombre_usu.insert(0, fila[0])
        self.cmb_rol.set(fila[1])
        self.entry_clave_usu.delete(0, tk.END)
        self.entry_clave_usu.insert(0, "********")
        self.btn_actualizar.config(state="normal")
        self.btn_eliminar.config(state="normal")

    def _al_presionar_enter(self, event):
        self._registrar_usuario()

    def _al_presionar_escape(self, event):
        self._limpiar_formulario_usu()

    def _al_cambiar_rol(self, event):
        pass

    # --- Operaciones CRUD ---
    def _registrar_usuario(self):
        nombre = self.entry_nombre_usu.get().strip()
        clave = self.entry_clave_usu.get().strip()
        rol = self.cmb_rol.get()
        if not nombre or not clave:
            messagebox.showwarning("Aviso", "Completa todos los campos")
            return
        if clave == "********":
            messagebox.showwarning("Aviso", "Escribe una contraseña nueva")
            return
        exito, mensaje = self.servicio.registrar_usuario(nombre, clave, rol)
        if exito:
            messagebox.showinfo("✅ Éxito", mensaje)
            self._limpiar_formulario_usu()
            self._actualizar_tabla_usuarios()
        else:
            messagebox.showerror("❌ Error", mensaje)

    def _actualizar_usuario(self):
        if not self.usuario_seleccionado:
            return
        nombre_nuevo = self.entry_nombre_usu.get().strip()
        clave = self.entry_clave_usu.get().strip()
        rol = self.cmb_rol.get()
        if clave == "********":
            datos = self.servicio.buscar_usuario(self.usuario_seleccionado)
            clave = datos["contrasena"]
        exito, mensaje = self.servicio.actualizar_usuario(self.usuario_seleccionado, nombre_nuevo, clave, rol)
        if exito:
            messagebox.showinfo("✅ Éxito", mensaje)
            self._limpiar_formulario_usu()
            self._actualizar_tabla_usuarios()
        else:
            messagebox.showerror("❌ Error", mensaje)

    def _eliminar_usuario(self):
        if not self.usuario_seleccionado:
            return
        if not messagebox.askyesno("Confirmar", f"¿Eliminar a {self.usuario_seleccionado}?"):
            return
        exito, mensaje = self.servicio.eliminar_usuario(self.usuario_seleccionado, self.usuario_actual)
        if exito:
            messagebox.showinfo("✅ Éxito", mensaje)
            self._limpiar_formulario_usu()
            self._actualizar_tabla_usuarios()
        else:
            messagebox.showerror("❌ Error", mensaje)

    def _limpiar_formulario_usu(self):
        self.entry_nombre_usu.delete(0, tk.END)
        self.entry_clave_usu.delete(0, tk.END)
        self.cmb_rol.set("Empleado")
        self.usuario_seleccionado = None
        self.btn_actualizar.config(state="disabled")
        self.btn_eliminar.config(state="disabled")
        self.tabla_usu.selection_remove(self.tabla_usu.selection())

    def _actualizar_tabla_usuarios(self):
        for fila in self.tabla_usu.get_children():
            self.tabla_usu.delete(fila)
        for u in self.servicio.listar_usuarios():
            self.tabla_usu.insert("", "end", values=(u["nombre_usuario"], u.get("rol", "Empleado")))

    # ============================================================
    # PRODUCTOS
    # ============================================================
    def _construir_productos(self):
        marco_form = ttk.LabelFrame(self.frame_productos, text="Datos del Producto")
        marco_form.pack(padx=15, pady=10, fill="x")

        ttk.Label(marco_form, text="ID:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.entry_id_prod = ttk.Entry(marco_form)
        self.entry_id_prod.grid(row=0, column=1, padx=5, pady=8)

        ttk.Label(marco_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=8, sticky="w")
        self.entry_nombre_prod = ttk.Entry(marco_form)
        self.entry_nombre_prod.grid(row=0, column=3, padx=5, pady=8)

        ttk.Label(marco_form, text="Precio ($):").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.entry_precio_prod = ttk.Entry(marco_form)
        self.entry_precio_prod.grid(row=1, column=1, padx=5, pady=8)

        ttk.Button(marco_form, text="Registrar", command=self._registrar_producto).grid(row=1, column=2, padx=10, pady=8)

        marco_lista = ttk.LabelFrame(self.frame_productos, text="Listado de Productos")
        marco_lista.pack(padx=15, pady=10, fill="both", expand=True)

        self.tabla_prod = ttk.Treeview(marco_lista, columns=("id", "nombre", "precio"), show="headings", height=10)
        for col in ["id", "nombre", "precio"]:
            self.tabla_prod.heading(col, text=col.title())
        self.tabla_prod.pack(fill="both", expand=True)
        self._actualizar_tabla_productos()

    def _registrar_producto(self):
        from modelos.producto import Producto
        try:
            prod = Producto(
                self.entry_id_prod.get().strip(),
                self.entry_nombre_prod.get().strip(),
                self.entry_precio_prod.get().strip()
            )
            if self.servicio.registrar_producto(prod):
                messagebox.showinfo("✅ Éxito", "Producto registrado")
                self.entry_id_prod.delete(0, tk.END)
                self.entry_nombre_prod.delete(0, tk.END)
                self.entry_precio_prod.delete(0, tk.END)
                self._actualizar_tabla_productos()
                self._recargar_combos()
            else:
                messagebox.showerror("❌ Error", "El ID ya existe")
        except Exception as e:
            messagebox.showerror("Datos incorrectos", str(e))

    def _actualizar_tabla_productos(self):
        for fila in self.tabla_prod.get_children():
            self.tabla_prod.delete(fila)
        for p in self.servicio.listar_productos():
            self.tabla_prod.insert("", "end", values=(p["id_producto"], p["nombre"], p["precio"]))

    # ============================================================
    # VENTAS
    # ============================================================
    def _construir_ventas(self):
        marco_form = ttk.LabelFrame(self.frame_ventas, text="Seleccionar Datos para la Venta")
        marco_form.pack(padx=15, pady=10, fill="x")

        ttk.Label(marco_form, text="Usuario:").grid(row=0, column=0, padx=5, pady=15, sticky="w")
        self.cmb_usuario = ttk.Combobox(marco_form, state="readonly", width=35)
        self.cmb_usuario.grid(row=0, column=1, padx=5, pady=15)

        ttk.Label(marco_form, text="Producto:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.cmb_producto = ttk.Combobox(marco_form, state="readonly", width=35)
        self.cmb_producto.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(marco_form, text="Registrar Venta", command=self._registrar_venta).grid(row=2, column=1, padx=5, pady=15)

        marco_lista = ttk.LabelFrame(self.frame_ventas, text="Historial de Ventas")
        marco_lista.pack(padx=15, pady=5, fill="both", expand=True)

        self.tabla_vent = ttk.Treeview(marco_lista, columns=("id", "usuario", "producto", "fecha"), show="headings", height=10)
        for col in ["id", "usuario", "producto", "fecha"]:
            self.tabla_vent.heading(col, text=col.title())
        self.tabla_vent.pack(fill="both", expand=True)

        self._recargar_combos()
        self._actualizar_tabla_ventas()

    def _recargar_combos(self):
        self.cmb_usuario["values"] = [u["nombre_usuario"] for u in self.servicio.listar_usuarios()]
        self.cmb_producto["values"] = [p["nombre"] for p in self.servicio.listar_productos()]
        if self.cmb_usuario["values"]:
            self.cmb_usuario.current(0)
        if self.cmb_producto["values"]:
            self.cmb_producto.current(0)

    def _registrar_venta(self):
        usuario = self.cmb_usuario.get().strip()
        producto = self.cmb_producto.get().strip()
        if not usuario or not producto:
            messagebox.showwarning("Aviso", "Selecciona usuario y producto")
            return
        exito, mensaje = self.servicio.registrar_venta(usuario, producto)
        if exito:
            messagebox.showinfo("✅ Venta Registrada", mensaje)
            self._actualizar_tabla_ventas()
        else:
            messagebox.showerror("❌ Error", mensaje)

    def _actualizar_tabla_ventas(self):
        for fila in self.tabla_vent.get_children():
            self.tabla_vent.delete(fila)
        for v in self.servicio.listar_ventas():
            self.tabla_vent.insert("", "end", values=(v["id_venta"], v["usuario"], v["producto"], v["fecha"]))

    def _salir(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Salir a la pantalla de inicio?"):
            for widget in self.root.winfo_children():
                widget.destroy()
            self.cerrar_sesion()