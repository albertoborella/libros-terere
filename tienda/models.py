from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre = models.CharField('Género', max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    descripcion = RichTextField()
    paginas = models.IntegerField()
    tapa = models.ImageField(upload_to='tapas/', null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField('En stock', default=True)

    def __str__(self):
        return self.titulo

class Presentacion(models.Model):
    texto = models.TextField()

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentación'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField('Correo electrónico')
    texto = models.TextField('Mensaje')

    def __str__(self):
        return nombre