from django.shortcuts import render


# Create your views here.
def index(request):
    content = {
        'title': 'geekshop'
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'title': 'geekshop'
    }
    return render(request, 'mainapp/products.html', context=content)
