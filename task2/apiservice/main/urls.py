from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import WbCardViewSet


router = DefaultRouter()
router.register(r'wb-card', WbCardViewSet)

urlpatterns = router.urls
