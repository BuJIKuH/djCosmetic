
from django.views.generic import ListView, DetailView
from rest_framework import generics

from news import serializers
from news.models import NewsModel


class NewsApiMixin:
    queryset = NewsModel.objects.all()
    serializer_class = serializers.NewsSerializer
    lookup_field = 'slug'


class NewsListApiView(NewsApiMixin, generics.ListCreateAPIView):
    """Вывод всех новостей"""
    ...


class NewsApiViewUpdate(NewsApiMixin, generics.RetrieveUpdateAPIView):
    """Вывод новости по slug"""
    ...


class NewsApiViewsDelete(NewsApiMixin, generics.RetrieveDestroyAPIView):
    """Удаление записей"""
    ...











