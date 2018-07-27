
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from catalog import views

urlpatterns = [
    #products
    path('<str:categoria_slug>', views.CategoryListView.as_view(), name='category'),
    path('produto/detalhes/<str:product_slug>', views.ProductDetailListView.as_view(), name='details'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    )
