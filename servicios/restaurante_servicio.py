from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_usuarios = "usuarios.json"
        self.inicializar_datos()

    def inicializar_datos(self):
        usuarios = ArchivoServicio.cargar_json(self.archivo_usuarios)
        if not usuarios:
            usuarios_defecto = [
                {"username": "admin", "password": "123", "rol": "Admin"},
                {"username": "mesero1", "password": "123", "rol": "Mesero"}
            ]
            ArchivoServicio.guardar_json(self.archivo_usuarios, usuarios_defecto)

    def autenticar(self, username, password):
        usuarios = ArchivoServicio.cargar_json(self.archivo_usuarios)
        for u in usuarios:
            if u["username"] == username and u["password"] == password:
                return u
        return None

    def obtener_usuarios(self):
        return ArchivoServicio.cargar_json(self.archivo_usuarios)
        # ====== MÉTODOS SEMANA 14: GESTIÓN DE PRODUCTOS ======
    def listar_productos(self):
        from servicios.archivo_servicio import ArchivoServicio
        return ArchivoServicio.cargar_json("datos/productos.json")

    def registrar_producto(self, id_producto, nombre, precio):
        from servicios.archivo_servicio import ArchivoServicio
        if not id_producto or not nombre or precio <= 0:
            return False
        productos = self.listar_productos()
        for p in productos:
            if p.get("id") == id_producto:
                return False
        productos.append({"id": id_producto, "nombre": nombre, "precio": precio})
        ArchivoServicio.guardar_json("datos/productos.json", productos)
        return True

    def buscar_producto(self, id_producto):
        productos = self.listar_productos()
        for p in productos:
            if p.get("id") == id_producto:
                return p
        return None

    def actualizar_producto(self, id_producto, nombre, precio):
        from servicios.archivo_servicio import ArchivoServicio
        if not id_producto or not nombre or precio <= 0:
            return False
        productos = self.listar_productos()
        for p in productos:
            if p.get("id") == id_producto:
                p["nombre"] = nombre
                p["precio"] = precio
                ArchivoServicio.guardar_json("datos/productos.json", productos)
                return True
        return False

    def eliminar_producto(self, id_producto):
        from servicios.archivo_servicio import ArchivoServicio
        productos = self.listar_productos()
        nueva_lista = [p for p in productos if p.get("id") != id_producto]
        if len(nueva_lista) < len(productos):
            ArchivoServicio.guardar_json("datos/productos.json", nueva_lista)
            return True
        return False