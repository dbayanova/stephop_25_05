from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contact', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request, pk=None):
    title = 'Продукты'

    products_ = Product.objects.all()  # .filter(category__name__in=['Джинсы', 'Кеды']).order_by('price')
    categories = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {
                'name': 'Все'
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_,
            'categories': categories,
            'category': category,
            'basket': basket,
        }

        return render(request, 'products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'products.html', context)


def product(request):
    title = 'Продукт'
    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'product.html', context)
