from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('news/', views.news_page, name='news'),
    # path('', views.NewsView.as_view(), name='home'),
    path('news/<str:slug>/', views.view_news, name='view_news'),

]