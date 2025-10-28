from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from app.event.view_form import add_event
from app.event.views import EventViewSet

router = DefaultRouter()
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('add-page/', TemplateView.as_view(template_name='event/add_event.html'), name='add_event_page'),
    path('add-event/', add_event, name='add_event'),
]
