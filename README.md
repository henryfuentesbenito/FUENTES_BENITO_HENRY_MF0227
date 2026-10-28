# Tienda — Catálogo de productos con Django

## Descripción del proyecto

Aplicación web desarrollada con Django que permite gestionar un catálogo sencillo de productos.

La aplicación permite:

- Registrar productos con nombre, precio y descuento.
- Almacenar los productos en una base de datos SQLite.
- Consultar el listado de productos registrados.
- Calcular automáticamente el precio final aplicando descuentos.
- Validar que los precios no sean negativos y que los descuentos estén entre 0 y 100 %.

El proyecto utiliza programación orientada a objetos mediante las clases `ProductoBase` y `ProductoOferta`.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML

## Instalación y ejecución

**1. Crear el entorno virtual**

```bash
python -m venv venv
```

**2. Activar el entorno virtual en Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**3. Instalar Django**

```bash
python -m pip install django
```

**4. Aplicar las migraciones**

```bash
python manage.py migrate
```

**5. Iniciar el servidor**

```bash
python manage.py runserver
```

**6. Acceder a la aplicación**

Listado de productos:

`http://127.0.0.1:8000/productos/`

Formulario para registrar productos:

`http://127.0.0.1:8000/productos/nuevo/`

## Pruebas automatizadas

Para ejecutar las pruebas:

```bash
python manage.py test catalogo
```

Se comprueba que:

1. Un producto de 100 € con un descuento del 20 % devuelve un precio final de 80 €.
2. La página `/productos/` responde con el código HTTP 200.

## Seguridad antes del despliegue en producción

Antes de desplegar la aplicación en producción, se debe establecer `DEBUG = False` en `settings.py` para evitar exponer información sensible de depuración a los usuarios.

También se deberá configurar correctamente `ALLOWED_HOSTS` con los dominios autorizados.

## Autor

Proyecto realizado como ejercicio práctico del módulo MF0227_3 — Programación orientada a objetos.