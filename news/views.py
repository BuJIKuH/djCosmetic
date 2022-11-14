from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from news.models import NewsModel


class NewsView(ListView):
    """Вывод всех новостей"""
    model = NewsModel
    template_name = 'news/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return NewsModel.objects.order_by('-date_create')


class NewsViewDetail(DetailView):
    """Вывод новости по slug"""
    model = NewsModel
    template_name = 'news/news_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'item'

    #111











