from django.urls import path, include
from .views import *
from rest_framework import routers, urlpatterns, views


router = routers.DefaultRouter()

router.register('groups', GroupViewSet)

urlpatterns = router.urls
