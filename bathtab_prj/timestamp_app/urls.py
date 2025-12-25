from django.urls import path
from . import views

urlpatterns = [
    path("", views.pee, name="pee"),
    path("pill/", views.pill, name="pill"),
]
