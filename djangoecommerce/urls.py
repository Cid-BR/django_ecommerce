"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))s
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.urls import include
from core import views

urlpatterns = [
    #core
    path('', views.ProductListView.as_view(), name='index'),
    path('contato', views.contact, name='contact'),
    path('sobre', views.about, name='about'),   
    path('admin/', admin.site.urls),

    #products
    path('categoria/', include('catalog.urls')),

    #accounts   
    path('conta/', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )
