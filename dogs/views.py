from django.shortcuts import render

from dogs.models import Dog, Category


def index(request):
    category_list = Category.objects.all()[:3]
    context = {
        'object_list': category_list,
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Питомник - все наши породы'
    }
    return render(request, 'dogs/categories.html', context)


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    dogs_list = Dog.objects.filter(category=pk)
    context = {
        'object_list': dogs_list,
        'title': f'Собаки породы {category_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)