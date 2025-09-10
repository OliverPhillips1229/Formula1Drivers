from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),


    path('drivers/', views.driver_index, name='driver-index'),
    path('drivers/<int:driver_id>/', views.driver_detail, name='driver-detail'),

    # Create/Update/Delete (CBVs)
    path('drivers/create/', views.DriverCreate.as_view(), name='driver-create'),
    path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='driver-delete'),
]