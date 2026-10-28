
from django.test import TestCase
from django.urls import reverse

from .dominio import ProductoOferta


class ProductoTests(TestCase):

    def test_precio_final_con_descuento(self):
        producto = ProductoOferta("Teclado", 100, 20)

        self.assertEqual(producto.precio_final(), 80)

    def test_listado_productos_responde_200(self):
        respuesta = self.client.get(
            reverse("lista_productos")
        )

        self.assertEqual(respuesta.status_code, 200)
