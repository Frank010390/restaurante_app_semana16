class Producto:
    def _init_(self, id_prod, nombre, precio, categoria):
        self.id = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos['id'], datos['nombre'], datos['precio'], datos['categoria']) 