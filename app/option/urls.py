from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from app.option.view_form import add_option
from app.option.views import OptionViewSet

router = DefaultRouter()
router.register(r'option', OptionViewSet, basename='option')

urlpatterns = [
    path('', include(router.urls)),
    path('add-page/', TemplateView.as_view(template_name='option/add_option.html'), name='add_option_page'),
    path('add-option/', add_option, name='add_option'),
]
