from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from app.category.view_form import add_category
from app.category.views import CategoryViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('add-page/', TemplateView.as_view(template_name='category/add_category.html'), name='add_category_page'),
    path('add-category/', add_category, name='add_category'),
]
