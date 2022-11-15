from django.urls import path

from news import views

urlpatterns = [
    path('api/v1/news/', views.NewsListApiView.as_view()),
    path('api/v1/news/<str:slug>/', views.NewsApiViewUpdate.as_view()),
    path('api/v1/news-destroy/<str:slug>/', views.NewsApiViewsDelete.as_view()),
    ]
