# from core.forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login_ctx_tag(request):
    return {'login_form' : AuthenticationForm()}