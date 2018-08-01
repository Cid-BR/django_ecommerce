from django.db import models
from django.core import validators
import re
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                    'Informe um nome de usuário válido. '
                    'Este valor deve conter apenas letras, números '
                    'e os caracteres: @/./+/-/_ .'
                    , 'invalid'
            )
        ], help_text = 'Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100)
    profile = models.ImageField('Profile Image', upload_to='profile', default = 'profile\generic-profile.jpg' )
    email = models.EmailField('E-mail', unique = True)
    
    logradouro = models.CharField('Logradouro', max_length=80, help_text='O seu endereço para envio de compra', blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=80, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=80, blank=True, null=True)
    estado = models.CharField('Estado', max_length=80, blank=True, null=True)
    pais = models.CharField('Páís', max_length=80, blank=True, null=True)
    cep = models.IntegerField('CEP', help_text='Código postal', blank=True, null=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default = True)
    date_joined = models.DateField('Data de entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

        def __str__(self):
            return self.name or self.username
        
    def get_full_name(self):
            return str(self)

    def get_short_name(self):
            return str(self).split(" ")[0]

