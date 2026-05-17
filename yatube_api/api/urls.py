from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import path, include

from .views import PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
