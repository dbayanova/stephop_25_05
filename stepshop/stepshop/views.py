from django.shortcuts import render

from mainapp.models import Product

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contact', 'name': 'Контакты', 'route': 'contact/'},
]


def index(request):
    title = 'Главная страница'

    products_ = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
    }

    return render(request, 'index.html', context)

    # return render(request=request, template_name='index.html', context=context)


def about(request):
    title = 'О нас'
    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'about.html', context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'contact.html', context)
