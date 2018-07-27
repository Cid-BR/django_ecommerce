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



