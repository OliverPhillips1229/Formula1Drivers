from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('drivers/', views.driver_index, name='driver-index'),
    path('drivers/<int:driver_id>/', views.driver_detail, name='driver-detail'),

    path('drivers/<int:driver_id>/associate-helmet/<int:helmet_id>/',
         views.associate_helmet, name='associate-helmet'),
    path('drivers/<int:driver_id>/remove-helmet/<int:helmet_id>/',
         views.remove_helmet, name='remove-helmet'),
    path(
    'drivers/<int:driver_id>/associate-helmet/<int:helmet_id>/',
    views.associate_helmet,
    name='associate-helmet'
    ),
    path(
    'drivers/<int:driver_id>/remove-helmet/<int:helmet_id>/',
    views.remove_helmet,
    name='remove-helmet'
    ),

    # Create/Update/Delete (CBVs)
    path('drivers/create/', views.DriverCreate.as_view(), name='driver-create'),
    path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='driver-delete'),
    path('drivers/<int:driver_id>/add-result/', views.add_result, name='add-result'),

    path('helmets/create/', views.HelmetCreate.as_view(), name='helmet-create'),
    path('helmets/<int:pk>/', views.HelmetDetail.as_view(), name='helmet-detail'),
    path('helmets/', views.HelmetList.as_view(), name='helmet-index'),
    path('helmets/<int:pk>/update/', views.HelmetUpdate.as_view(), name='helmet-update'),
    path('helmets/<int:pk>/delete/', views.HelmetDelete.as_view(), name='helmet-delete'),
]