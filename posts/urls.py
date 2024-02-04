"""
URL mappings for post app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from posts import views


router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('tags', views.TagViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
]