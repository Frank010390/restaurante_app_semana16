class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self._nombre_usuario = nombre_usuario
        self._contrasena = contrasena

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @property
    def contrasena(self):
        return self._contrasena

    def to_dict(self):
        return {
            "nombre_usuario": self._nombre_usuario,
            "contrasena": self._contrasena
        }