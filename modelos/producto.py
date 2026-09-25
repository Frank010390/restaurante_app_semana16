class Producto:
    def __init__(self, id_producto, nombre, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = float(precio)

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def to_dict(self):
        return {
            "id_producto": self._id_producto,
            "nombre": self._nombre,
            "precio": self._precio
        }