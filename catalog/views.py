from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views import generic


#models
from catalog.models import Product
from catalog.models import Category
from django.contrib.auth.models import User



class ProductDetailListView(generic.ListView):

    model = Product
    context_object_name = 'product'
    template_name = 'product-details.html'

    def get_queryset(self):
        return Product.objects.get(slug=self.kwargs['product_slug'])

  


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