class Usuario:
    def __init__(self, nombre_usuario, contrasena, rol="Empleado"):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol  # Administrador, Empleado, Cliente

    def to_dict(self):
        return {
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }