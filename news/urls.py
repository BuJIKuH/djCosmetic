from django.urls import path

from news import views

urlpatterns = [
    path('', views.NewsView.as_view(), name='news'),
    path('news/<str:slug>/', views.NewsViewDetail.as_view(), name='view_news'),
    ]
