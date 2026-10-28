
from django.shortcuts import render, redirect

from .models import Producto
from .forms import ProductoForm
from .dominio import ProductoOferta


def lista_productos(request):
    productos = Producto.objects.all()

    lista = []

    for producto in productos:
        producto_oferta = ProductoOferta(
            producto.nombre,
            producto.precio,
            producto.descuento
        )

        lista.append({
            "nombre": producto.nombre,
            "precio": producto.precio,
            "descuento": producto.descuento,
            "precio_final": producto_oferta.precio_final()
        })

    return render(
        request,
        "catalogo/lista_productos.html",
        {"productos": lista}
    )


def nuevo_producto(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_productos")

    else:
        formulario = ProductoForm()

    return render(
        request,
        "catalogo/nuevo_producto.html",
        {"formulario": formulario}
    )
