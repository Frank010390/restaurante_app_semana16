from datetime import datetime

class Venta:
    def __init__(self, id_venta, usuario, producto):
        self._id_venta = id_venta
        self._usuario = usuario
        self._producto = producto
        self._fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def id_venta(self):
        return self._id_venta

    @property
    def usuario(self):
        return self._usuario

    @property
    def producto(self):
        return self._producto

    @property
    def fecha(self):
        return self._fecha

    def to_dict(self):
        return {
            "id_venta": self._id_venta,
            "usuario": self._usuario,
            "producto": self._producto,
            "fecha": self._fecha
        }