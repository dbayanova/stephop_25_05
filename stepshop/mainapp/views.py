from django.shortcuts import render
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contact', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request):
    title = 'Продукты'

    products_ = Product.objects.all()  # .filter(category__name__in=['Джинсы', 'Кеды']).order_by('price')
    categories = ProductCategory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
    }

    return render(request, 'products.html', context)


def product(request):
    title = 'Продукт'
    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'product.html', context)
