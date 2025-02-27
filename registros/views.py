
from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro
from .forms import RegistroForm

# Listar registros (READ)
def lista_registros(request):
    registros = Registro.objects.all()
    return render(request, 'registros/lista_registros.html', {'registros': registros})

# Crear registro (CREATE)
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'registros/crear_registro.html', {'form': form})

# Editar registro (UPDATE)
def editar_registro(request, id):
    registro = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registros/editar_registro.html', {'form': form})

# Eliminar registro (DELETE)
def eliminar_registro(request, id):
    registro = get_object_or_404(Registro, id=id)
    registro.delete()
    return redirect('lista_registros')