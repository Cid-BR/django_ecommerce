from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views import generic
#Authentication
from django.contrib.auth import authenticate, login
#forms
from core.forms import ContactForm
from core.forms import LoginForm
#models
from catalog.models import Product
from catalog.models import Category
from django.contrib.auth.models import User

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'
    paginate_by = 6

class ProductDetailListView(generic.ListView):

    model = Product
    produtc = 'product'
    template_name = 'product-details.html'


    def get_queryset(self):
        return Product.objects.get(slug=self.kwargs['produto_slug'])

'''
    def get_context_data(self, **kwargs):
        context = super(ProductDetailListView, self).get_context_data(**kwargs)
        context['rangeStars'] = range(4)
        context['rangeNotStars'] = range(1)
        context['product'] = product
'''


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
    paginate_by = 6


    def get_queryset(self):
        return Product.objects.filter(category__slug = self.kwargs['categoria_slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categoria'] = get_object_or_404(Category, slug=self.kwargs['categoria_slug'])
        return context

