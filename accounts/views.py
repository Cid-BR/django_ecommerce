from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import User
class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
    

class UserDetailsListView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class UpdateUserView(UpdateView):

    model = User
    template_name = 'accounts/update_account.html'
    fields = ['email', 'username']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class UpdatePersonalView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_personal.html'
    fields = ['email', 'username', 'password']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('profile')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)