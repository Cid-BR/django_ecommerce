from core.forms import LoginForm
from django.shortcuts import render
# from allauth.account.forms import LoginForm

def login_ctx_tag(request):
    return {'login_form' : LoginForm()}