

from decimal import Decimal


class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = Decimal(str(precio))

        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

    def precio_final(self):
        return self.precio


class ProductoOferta(ProductoBase):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def precio_final(self):
        return self.precio * (
            Decimal("1") -
            Decimal(str(self.descuento)) / Decimal("100")
        )

