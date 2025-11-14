from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriaForm, ProductoForm
from .models import Categoria, Producto

def index(request):
    return render(request, "appFinal/index.html")
# --------- CATEGORIAS ----------
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "appFinal/categorias.html", {"categorias": categorias})


def agregar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("listar_categorias")
    return render(request, "appFinal/agregar_categoria.html", {"form": form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("listar_categorias")
    return render(request, "appFinal/editar_categoria.html", {"form": form})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect("listar_categorias")

# --------- PRODUCTOS ----------
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "appFinal/productos.html", {"productos": productos})


def agregar_producto(request):
    form = ProductoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    return render(request, "appFinal/agregar_producto.html", {"form": form})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    return render(request, "appFinal/editar_producto.html", {"form": form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect("listar_productos")

def creditos(request):
    return render(request, "appFinal/creditos.html")