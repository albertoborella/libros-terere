from django.shortcuts import render
from .models import Libro,Categoria,Presentacion
from .forms import ContactoForm

def index(request):
    context = {}
    return render(request, 'tienda/index.html', context)

def libro(request, id):
    libro = Libro.objects.get(id=id)
    context = { 'libro':libro}
    return render(request, 'tienda/info.html', context)

def cronica(request, categoria_id):
    libros_cronica = Libro.objects.filter(categoria_id=1)
    titulo = 'CRONICA'
    context = {'libros_cronica':libros_cronica, 'titulo':titulo}
    return render(request, 'tienda/cronica.html', context)

def narrativa(request, categoria_id):
    libros_narrativa = Libro.objects.filter(categoria_id=2)
    titulo = 'NARRATIVA'
    context = {'libros_narrativa':libros_narrativa, 'titulo':titulo}
    return render(request, 'tienda/narrativa.html', context)

def ensayo(request, categoria_id):
    libros_ensayo = Libro.objects.filter(categoria_id=3)
    context = {'libros_ensayo':libros_ensayo}
    return render(request, 'tienda/ensayo.html', context)

def poesia(request, categoria_id):
    libros_poesia = Libro.objects.filter(categoria_id=4)
    context = {'libros_poesia':libros_poesia}
    return render(request, 'tienda/poesia.html', context)

def blog(request):
    context = {}
    return render(request, 'tienda/blog.html', context)

def terere(request):
    texto = Presentacion.objects.all()
    context = {'texto':texto}
    return render(request, 'tienda/terere.html', context)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje']='Contacto guardado'
        else:
            data[form]=form
    return render(request, 'tienda/contacto.html', data)
