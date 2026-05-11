import datetime
import pytz
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from markupsafe import Markup
from flask import url_for
from flask_appbuilder.filemanager import ImageManager

# Configurar zona horaria de Bolivia (UTC-4)
def get_bolivia_time():
    bolivia_tz = pytz.timezone('America/La_Paz')
    return datetime.datetime.now(bolivia_tz)

class Categoria(Model):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(ImageColumn(thumbnail_size=(50, 50, True)), nullable=True)  # ← Usar ImageColumn
    estado = Column(Boolean, nullable=True, default=True)
    creado_en = Column(DateTime, default=get_bolivia_time, nullable=False)
    actualizado_en = Column(DateTime, default=get_bolivia_time, onupdate=get_bolivia_time, nullable=False)
    
    productos = relationship("Producto", back_populates="categoria")
    
    def foto_thumbnail(self):
        """Método para mostrar miniatura de la imagen"""
        im = ImageManager()
        if self.imagen:
            return Markup(
                f'<img src="{im.get_url_thumbnail(self.imagen)}" '
                f'width="50" height="50" style="object-fit: cover; border-radius: 4px;">'
            )
        return Markup('<span class="label label-default">Sin imagen</span>')
    
    def __repr__(self):
        return self.nombre

class Producto(Model):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    imagen = Column(ImageColumn(thumbnail_size=(50, 50, True)), nullable=True)  # ← Usar ImageColumn
    estado = Column(Boolean, nullable=True, default=True)
    creado_en = Column(DateTime, default=get_bolivia_time, nullable=False)
    actualizado_en = Column(DateTime, default=get_bolivia_time, onupdate=get_bolivia_time, nullable=False)
    
    categoria = relationship("Categoria", back_populates="productos")
    
    def foto_thumbnail(self):
        """Método para mostrar miniatura de la imagen"""
        im = ImageManager()
        if self.imagen:
            return Markup(
                f'<img src="{im.get_url_thumbnail(self.imagen)}" '
                f'width="50" height="50" style="object-fit: cover; border-radius: 4px;">'
            )
        return Markup('<span class="label label-default">Sin imagen</span>')
    
    def __repr__(self):
        return self.nombre