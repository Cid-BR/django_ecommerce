

from .models import Category
from .models import Product

def categories(request):
    return {
        'categories'  : Category.objects.all(),
    }

