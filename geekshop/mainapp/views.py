from django.shortcuts import render
import json, os

from .models import ProductCategory, Product

CURENT_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    content = {
        'title': 'geekshop'
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    # catalog_path = os.path.join(CURENT_DIR, 'fixtures/catalog.json')
    # with open(catalog_path, 'r', encoding='utf-8') as f:
    #     content = {
    #         'title': 'geekshop',
    #         'things': json.load(f)
    #     }
    title ='каталог'
    products = Product.objects.all()
    productsCategory = ProductCategory.objects.all()
    content = {'title':title, 'things':products, 'categores':productsCategory}
    return render(request, 'mainapp/products.html', context=content)

