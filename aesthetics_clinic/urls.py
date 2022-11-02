from django.urls import path

from aesthetics_clinic import views

urlpatterns = [
    path('procedures/', views.ProceduresView.as_view(), name='procedures'),
    path('masters/', views.MasterView.as_view(), name='masters'),
    path('procedures/<str:slug>/', views.ProceduresViewDetail.as_view(), name='view_procedures'),
    path('masters/<str:slug>/', views.MasterViewDetail.as_view(), name='view_master'),

    ]