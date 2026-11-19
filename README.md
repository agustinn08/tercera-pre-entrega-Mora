# Tienda de zapatillas – Django

Aplicación web hecha con Django para administrar un catálogo de zapatillas. Incluye usuarios, CRUD completo y búsqueda. Proyecto del curso de Python y Django de Coderhouse.

## Funcionalidades

- Alta, listado, edición y eliminación de zapatillas (nombre, modelo, marca, talle e imagen)
- Búsqueda de productos
- Registro, inicio y cierre de sesión de usuarios
- Avatar de usuario y publicaciones con imagen
- Modelos relacionados: clientes, países, zapatillas y posts

## Tecnologías

- Python 3 y Django
- SQLite
- Plantillas HTML y CSS

## Cómo ejecutarlo

```bash
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py runserver
```

Luego abrir `http://127.0.0.1:8000/`.

## Estructura

```
cliente/   app principal (modelos, vistas, formularios, plantillas)
core/      plantillas base y archivos estáticos
config/    configuración del proyecto
```

## Autor

Agustín Mora · Técnico en Informática · Full Stack en formación
