from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserAdminCreationForm
from django.views import generic
from django.urls import reverse_lazy


from .models import User
class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
    

class UserDetailsListView(generic.ListView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'