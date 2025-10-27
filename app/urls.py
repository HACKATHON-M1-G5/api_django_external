from django.urls import path, include

urlpatterns = [
    path("event/", include("app.event.urls")),
    path("option/", include("app.option.urls")),
    path("category/", include("app.category.urls")),
]
