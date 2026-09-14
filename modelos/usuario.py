class Usuario:
    def _init_(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos['username'], datos['password'], datos['rol'])