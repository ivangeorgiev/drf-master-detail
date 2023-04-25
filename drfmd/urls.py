# urls.py

from django.urls import path, include
from rest_framework import routers
from .views import MasterViewSet, DetailViewSet

router = routers.DefaultRouter()
router.register(r'master', MasterViewSet)
router.register(r'detail', DetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

