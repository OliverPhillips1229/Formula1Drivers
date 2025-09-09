from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('drivers/', views.driver_index, name='driver_index'),
    path('drivers/<int:driver_id>/', views.driver_detail, name='driver_detail'),
]