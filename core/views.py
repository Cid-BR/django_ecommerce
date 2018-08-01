from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import FormView
from django.urls import reverse_lazy
#Authentication
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

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

class About(generic.TemplateView):
    template_name = 'about.html'

def Contact(request):
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


# class Contact(LoginRequiredMixin, FormView):
#     template_name = 'contact.html'
#     success_url = reverse_lazy('index')
#     form_class = ContactForm

#     def form_valid(self):
#         form.save()
#         return super(Contact, self).form_valid(form)

