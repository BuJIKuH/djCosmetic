from django.urls import path

from aesthetics_clinic import views

urlpatterns = [
    path('procedures/', views.ProceduresView.as_view(), name='procedures'),
    path('procedures/<str:slug>/', views.ProceduresViewDetail.as_view(), name='view_procedures'),

    ]