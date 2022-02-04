from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    context_dict = {}
    category_list = Category.objects.order_by('-likes')[:5]
    popular_list = Page.objects.order_by('-views')[:5]
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['popular'] = popular_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'MEDIA_URL': '/media/'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
