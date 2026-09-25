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