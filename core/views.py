from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from catalog.models import Product
from catalog.models import Category
from core.forms import ContactForm
from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'


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

class CategoryListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug = self.kwargs['categoria_slug'])


def quantidadeRelativaCategoria(categoria):
   return{
       'notebooks' : 5,
       'acessorio' : 12,
       'celular' : 3
   }.get(categoria.lower(), 9)