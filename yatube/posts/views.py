from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    heading = 'Это главная страница проекта Yatube'
    context = {
        'heading': heading
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    heading = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'heading': heading
    }
    return render(request, template, context)
