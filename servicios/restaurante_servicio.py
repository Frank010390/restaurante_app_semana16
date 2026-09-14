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
