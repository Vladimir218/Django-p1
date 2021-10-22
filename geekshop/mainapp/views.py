from django.shortcuts import render
import json, os

from .models import ProductCategory, Product
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

CURENT_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    content = {
        'title': 'geekshop'
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request,category_id = None, page_id=1):
    # catalog_path = os.path.join(CURENT_DIR, 'fixtures/catalog.json')
    # with open(catalog_path, 'r', encoding='utf-8') as f:
    #     content = {
    #         'title': 'geekshop',
    #         'things': json.load(f)
    #     }
    title ='Каталог'
    products = Product.objects.filter(category_id = category_id)  if category_id != None else Product.objects.all()
    paginator = Paginator(products,per_page=2)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(Paginator.num_pages)

    productsCategory = ProductCategory.objects.all()
    content = {'title':title,
               'categores':productsCategory}
    content.update({'things':products_paginator})
    return render(request, 'mainapp/products.html', context=content)

