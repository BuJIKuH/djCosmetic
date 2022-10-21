from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from news.models import NewsModel


def news_page(request):
    news = NewsModel.objects.all()
    return render(request, 'news/news.html', {'news': news, 'title': 'Список новостей'})


def view_news(request, slug):
    item = NewsModel.objects.get(slug=slug)
    return render(request, 'news/news_detail.html', {'item': item})










