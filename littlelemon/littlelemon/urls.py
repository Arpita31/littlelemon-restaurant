from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')
router.register(r'users', views.UserViewSet, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    #add following lines to update urlpatterns list
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api-token-auth/', obtain_auth_token),
]
