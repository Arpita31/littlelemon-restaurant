from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    
]
