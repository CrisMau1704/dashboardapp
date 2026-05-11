import os
from flask import url_for
from markupsafe import Markup
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.filemanager import ImageManager

from .models import Categoria, Producto
from .extensions import appbuilder

class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    
    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripcion",
        "imagen": "Imagen",
        "estado": "Estado",
        "creado_en": "Creado en",
        "actualizado_en": "Actualizado en"
    }
    
    # Usar el método foto_thumbnail para mostrar la imagen
    list_columns = ["nombre", "descripcion", "foto_thumbnail", "estado", "creado_en"]
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen", "estado", "creado_en", "actualizado_en"]
    
    # Configurar el nombre mostrado para la columna
    label_columns['foto_thumbnail'] = "Imagen"

class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    
    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripcion",
        "precio": "Precio (Bs)",
        "categoria": "Categoria",
        "imagen": "Imagen",
        "estado": "Estado",
        "creado_en": "Creado en",
        "actualizado_en": "Actualizado en"
    }
    
    # Usar el método foto_thumbnail para mostrar la imagen
    list_columns = ["nombre", "precio", "categoria", "foto_thumbnail", "estado"]
    add_columns = ["nombre", "descripcion", "precio", "categoria", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "precio", "categoria", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "categoria", "imagen", "estado", "creado_en", "actualizado_en"]
    
    # Configurar el nombre mostrado para la columna
    label_columns['foto_thumbnail'] = "Imagen"

# Agregar las vistas
appbuilder.add_view(
    CategoriaModelView,
    "Categorias",
    icon="fa-folder",
    category="Configuraciones",
    category_icon="fa-cogs"
)

appbuilder.add_view(
    ProductoModelView,
    "Productos",
    icon="fa-shopping-cart",
    category="Configuraciones",
    category_icon="fa-cogs"
)