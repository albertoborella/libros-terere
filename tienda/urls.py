from django.urls import path
from .views import index,libro,cronica,ensayo,poesia,narrativa,blog,terere,contacto

app_name = 'tienda'

urlpatterns=[
    path('', index, name='index'),
    path('libro/<int:id>/', libro, name='libro'),
    # path('libros/<int:categoria_id>/', libros, name='libros'),
    path('ensayo/<int:categoria_id>/', ensayo, name='ensayo'),
    path('poesia/<int:categoria_id>/', poesia, name='poesia'),
    path('narrativa/<int:categoria_id>/', narrativa, name='narrativa'),
    path('cronica/<int:categoria_id>/', cronica, name='cronica'),
    path('blog/', blog, name='blog'),
    path('terere/', terere, name='terere'),
    path('contacto/', contacto, name='contacto'),
]