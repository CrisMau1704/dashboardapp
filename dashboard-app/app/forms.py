from flask_appbuilder.fieldwidgets import BS3FileFieldWidget
from wtforms import FileField
from flask_appbuilder.forms import DynamicForm

class CategoriaForm(DynamicForm):
    nombre = None  # Esto se hereda automáticamente
    descripcion = None
    imagen = FileField("Imagen", widget=BS3FileFieldWidget())
    estado = None

class ProductoForm(DynamicForm):
    nombre = None
    descripcion = None
    precio = None
    categoria = None
    imagen = FileField("Imagen", widget=BS3FileFieldWidget())
    estado = None