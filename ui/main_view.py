import tkinter as tk
from tkinter import ttk, messagebox
from modelos.producto import Producto

class MainView:
    def __init__(self, root, servicio, usuario_actual, callback_cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = callback_cerrar_sesion

        self.root.title("🍽️ Gestión de Restaurante — Semana 13")
        self.root.geometry("900x600")

        self.cuaderno = ttk.Notebook(root)
        self.cuaderno.pack(pady=15, padx=15, fill="both", expand=True)

        self.frame_usuarios = ttk.Frame(self.cuaderno)
        self.frame_productos = ttk.Frame(self.cuaderno)
        self.frame_ventas = ttk.Frame(self.cuaderno)

        self.cuaderno.add(self.frame_usuarios, text="👥 Usuarios")
        self.cuaderno.add(self.frame_productos, text="📦 Productos")
        self.cuaderno.add(self.frame_ventas, text="💰 Ventas")

        # === Cargar imágenes ===
        try:
            self.icono_app = tk.PhotoImage(file="assets/icons/icono.png")
            self.root.iconphoto(True, self.icono_app)

            self.logo_app = tk.PhotoImage(file="assets/logo/logo.png")
            ttk.Label(self.frame_usuarios, image=self.logo_app).pack(pady=10)
        except Exception as e:
            print(f"No se pudieron cargar las imágenes: {e}")
        # === Fin imágenes ===

        self._construir_usuarios()
        self._construir_productos()
        self._construir_ventas()
        self._actualizar_tabla_usuarios()
        self._actualizar_tabla_productos()
        self._recargar_combos()
        self._actualizar_tabla_ventas()

    def _construir_usuarios(self):
        ttk.Label(self.frame_usuarios, text=f"Bienvenido: {self.usuario_actual}", font=("Arial", 12, "bold")).pack(pady=15)
        ttk.Label(self.frame_usuarios, text="Usuarios registrados en el sistema").pack(pady=5)
        self.tabla_usu = ttk.Treeview(self.frame_usuarios, columns=("usuario",), show="headings", height=10)
        self.tabla_usu.heading("usuario", text="Nombre de Usuario")
        self.tabla_usu.column("usuario", width=350)
        self.tabla_usu.pack(pady=10, padx=20, fill="both", expand=True)
        ttk.Button(self.frame_usuarios, text="Cerrar Sesión", command=self._salir).pack(pady=10)

    def _actualizar_tabla_usuarios(self):
        for fila in self.tabla_usu.get_children():
            self.tabla_usu.delete(fila)
        for u in self.servicio.listar_usuarios():
            self.tabla_usu.insert("", "end", values=(u["nombre_usuario"],))

    def _salir(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Salir a la pantalla de inicio?"):
            # Limpiamos antes de cerrar para evitar error
            for widget in self.root.winfo_children():
                widget.destroy()
            self.cerrar_sesion()

    def _construir_productos(self):
        marco_form = ttk.LabelFrame(self.frame_productos, text="Datos del Producto")
        marco_form.pack(padx=15, pady=10, fill="x")
        ttk.Label(marco_form, text="ID:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.entry_id = ttk.Entry(marco_form)
        self.entry_id.grid(row=0, column=1, padx=5, pady=8)
        ttk.Label(marco_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=8, sticky="w")
        self.entry_nombre = ttk.Entry(marco_form)
        self.entry_nombre.grid(row=0, column=3, padx=5, pady=8)
        ttk.Label(marco_form, text="Precio ($):").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.entry_precio = ttk.Entry(marco_form)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=8)
        ttk.Button(marco_form, text="Registrar", command=self._registrar_producto).grid(row=1, column=2, padx=10, pady=8)

        marco_lista = ttk.LabelFrame(self.frame_productos, text="Listado de Productos")
        marco_lista.pack(padx=15, pady=10, fill="both", expand=True)
        self.tabla_prod = ttk.Treeview(marco_lista, columns=("id", "nombre", "precio"), show="headings", height=10)
        for c in ["id", "nombre", "precio"]:
            self.tabla_prod.heading(c, text=c.title())
        self.tabla_prod.pack(fill="both", expand=True)

    def _actualizar_tabla_productos(self):
        for fila in self.tabla_prod.get_children():
            self.tabla_prod.delete(fila)
        for p in self.servicio.listar_productos():
            self.tabla_prod.insert("", "end", values=(p["id_producto"], p["nombre"], p["precio"]))

    def _registrar_producto(self):
        try:
            prod = Producto(self.entry_id.get().strip(), self.entry_nombre.get().strip(), self.entry_precio.get().strip())
            if self.servicio.registrar_producto(prod):
                messagebox.showinfo("✅ Éxito", "Producto registrado")
                self.entry_id.delete(0, tk.END)
                self.entry_nombre.delete(0, tk.END)
                self.entry_precio.delete(0, tk.END)
                self._actualizar_tabla_productos()
                self._recargar_combos()
            else:
                messagebox.showerror("❌ Error", "El ID ya existe")
        except Exception as e:
            messagebox.showerror("Datos incorrectos", str(e))

    def _construir_ventas(self):
        marco_form = ttk.LabelFrame(self.frame_ventas, text="Seleccionar Datos para la Venta")
        marco_form.pack(padx=15, pady=10, fill="x")
        ttk.Label(marco_form, text="Usuario:").grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.cmb_usuario = ttk.Combobox(marco_form, state="readonly", width=35)
        self.cmb_usuario.grid(row=0, column=1, padx=5, pady=15)
        ttk.Label(marco_form, text="Producto:").grid(row=1, column=0, padx=15, pady=5, sticky="w")
        self.cmb_producto = ttk.Combobox(marco_form, state="readonly", width=35)
        self.cmb_producto.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(marco_form, text="✅ Registrar Venta", command=self._registrar_venta).grid(row=2, column=1, padx=5, pady=15)

        marco_lista = ttk.LabelFrame(self.frame_ventas, text="Historial de Ventas")
        marco_lista.pack(padx=15, pady=5, fill="both", expand=True)
        self.tabla_vent = ttk.Treeview(marco_lista, columns=("id", "usuario", "producto", "fecha"), show="headings", height=10)
        for c in ["id", "usuario", "producto", "fecha"]:
            self.tabla_vent.heading(c, text=c.title())
        self.tabla_vent.pack(fill="both", expand=True)

    def _recargar_combos(self):
        self.cmb_usuario["values"] = [u["nombre_usuario"] for u in self.servicio.listar_usuarios()]
        self.cmb_producto["values"] = [p["nombre"] for p in self.servicio.listar_productos()]
        if self.cmb_usuario["values"]: self.cmb_usuario.current(0)
        if self.cmb_producto["values"]: self.cmb_producto.current(0)

    def _registrar_venta(self):
        usuario = self.cmb_usuario.get().strip()
        producto = self.cmb_producto.get().strip()
        if not usuario:
            messagebox.showwarning("Aviso", "Selecciona un usuario")
            return
        if not producto:
            messagebox.showwarning("Aviso", "Selecciona un producto")
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