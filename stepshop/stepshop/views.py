from django.shortcuts import render


def index(request):
    title = 'Главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

    # return render(request=request, template_name='index.html', context=context)


def about(request):
    title = 'О нас'
    context = {
        'title': title,
    }

    return render(request, 'about.html', context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title
    }

    return render(request, 'contact.html', context)
