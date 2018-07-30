from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns =[
    path('adicionar/<str:slug>', views.CreateCartItemView.as_view(), name='create_cartitem')
]