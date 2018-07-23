from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
from catalog.models import Category
from core.forms import ContactForm
from django.views import generic

def index(request):
    context = {
        'products'    : Product.objects.all(),
    }
    return render(request, 'index.html', context )

def details(request, produto_slug):
    produto_selecionado = Product.objects.get(slug = produto_slug )
    context = {
        'product' : produto_selecionado,
        'rangeStars' : range(produto_selecionado.stars),
        'rangeNotStars' : range(5-produto_selecionado.stars),
    }
    
    return render(request, 'product-details.html', context)

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucess = True
    context = {
       'form' : form,
       'success' : success
    }
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def categories(request, categoria_slug):
    category = Category.objects.get(slug = categoria_slug)
    context = {
        'categoria' : categoria_slug.capitalize(),
        'products'  : Product.objects.filter(category_id = category.id),
        }
    return render(request, 'index.html', context)

def quantidadeRelativaCategoria(categoria):
   return{
       'notebooks' : 5,
       'acessorio' : 12,
       'celular' : 3
   }.get(categoria.lower(), 9)