from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea) 
        

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome:{0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail('Contato do Django E-commerce', message, settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL]
        )

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', 
        widget= forms.TextInput(attrs = {'placeholder' : 'Username'} )
    )
    password = forms.CharField(label='Password', max_length=16,
        widget = forms.PasswordInput(attrs = {'placeholder':'senha'}, 
        render_value = False),
        validators=[MinLengthValidator(8, message = 'A senha deve conterao menos 8 caracteres')]
    )