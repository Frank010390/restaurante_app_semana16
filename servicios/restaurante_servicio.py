from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo = ArchivoServicio()

    def validar_usuario(self, nombre_usuario, contrasena):
        usuarios = self.archivo.cargar_json("datos/usuarios.json")
        for u in usuarios:
            if u["nombre_usuario"] == nombre_usuario and u["contrasena"] == contrasena:
                return True
        return False

    def listar_usuarios(self):
        return self.archivo.cargar_json("datos/usuarios.json")

    def registrar_producto(self, producto: Producto):
        productos = self.archivo.cargar_json("datos/productos.json")
        if any(p["id_producto"] == producto.id_producto for p in productos):
            return False
        productos.append(producto.to_dict())
        self.archivo.guardar_json("datos/productos.json", productos)
        return True

    def listar_productos(self):
        return self.archivo.cargar_json("datos/productos.json")

    def registrar_venta(self, nombre_usuario, nombre_producto):
        usuarios = self.listar_usuarios()
        productos = self.listar_productos()
        ventas = self.archivo.cargar_json("datos/ventas.json")

        if not any(u["nombre_usuario"] == nombre_usuario for u in usuarios):
            return False, f"Usuario '{nombre_usuario}' no existe"
        if not any(p["nombre"] == nombre_producto for p in productos):
            return False, f"Producto '{nombre_producto}' no existe"

        ultimo_id = max([v["id_venta"] for v in ventas], default=0)
        venta = Venta(ultimo_id + 1, nombre_usuario, nombre_producto)
        ventas.append(venta.to_dict())
        self.archivo.guardar_json("datos/ventas.json", ventas)
        return True, f"Venta registrada ✅ ID: {ultimo_id + 1}"

    def listar_ventas(self):
        return self.archivo.cargar_json("datos/ventas.json")
            # ============================================================
    # NUEVOS — Gestión de Usuarios (Semana 16)
    # ============================================================
    def buscar_usuario(self, nombre_usuario):
        """Busca un usuario y devuelve sus datos o None"""
        usuarios = self.listar_usuarios()
        for u in usuarios:
            if u["nombre_usuario"] == nombre_usuario:
                return u
        return None

    def registrar_usuario(self, nombre_usuario, contrasena, rol="Empleado"):
        """Registra usuario nuevo → (exito, mensaje)"""
        usuarios = self.listar_usuarios()
        
        # Validar que no exista
        if any(u["nombre_usuario"] == nombre_usuario for u in usuarios):
            return False, f"El usuario '{nombre_usuario}' ya existe"
        
        # Crear con el modelo Usuario
        nuevo = Usuario(nombre_usuario, contrasena, rol)
        usuarios.append(nuevo.to_dict())
        self.archivo.guardar_json("datos/usuarios.json", usuarios)
        return True, f"Usuario '{nombre_usuario}' registrado como {rol}"

    def actualizar_usuario(self, nombre_antiguo, nombre_nuevo, contrasena_nueva, rol_nuevo):
        """Modifica datos de usuario existente"""
        usuarios = self.listar_usuarios()
        
        # Si cambia el nombre, verificar que no esté ocupado
        if nombre_nuevo != nombre_antiguo:
            if any(u["nombre_usuario"] == nombre_nuevo for u in usuarios):
                return False, f"El nombre '{nombre_nuevo}' ya está en uso"
        
        # Buscar y reemplazar
        for i, u in enumerate(usuarios):
            if u["nombre_usuario"] == nombre_antiguo:
                usuarios[i] = {
                    "nombre_usuario": nombre_nuevo,
                    "contrasena": contrasena_nueva,
                    "rol": rol_nuevo
                }
                self.archivo.guardar_json("datos/usuarios.json", usuarios)
                return True, f"Usuario actualizado: {nombre_nuevo}"
        
        return False, f"No se encontró a {nombre_antiguo}"

    def eliminar_usuario(self, nombre_a_eliminar, usuario_actual):
        """Borra usuario con protección: NO puedes borrarte a ti mismo"""
        if nombre_a_eliminar == usuario_actual:
            return False, "❌ No puedes eliminar tu propia cuenta"
        
        usuarios = self.listar_usuarios()
        filtrados = [u for u in usuarios if u["nombre_usuario"] != nombre_a_eliminar]
        
        if len(filtrados) == len(usuarios):
            return False, f"No se encontró a {nombre_a_eliminar}"
        
        self.archivo.guardar_json("datos/usuarios.json", filtrados)
        return True, f"Usuario '{nombre_a_eliminar}' eliminado ✅"