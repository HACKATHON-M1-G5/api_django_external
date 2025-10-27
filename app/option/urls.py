from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OptionViewSet

router = DefaultRouter()
router.register(r'', OptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
