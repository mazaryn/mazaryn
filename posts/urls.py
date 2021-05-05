from django.urls import path, include
from .views import *
from rest_framework import routers, urlpatterns, views


router = routers.DefaultRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
