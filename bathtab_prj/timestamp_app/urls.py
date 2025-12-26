from django.urls import path
from . import views

urlpatterns = [
    path("", views.pee, name="pee"),
    path("pill/", views.pill, name="pill"),
    path("weight/", views.WeightListView.as_view(), name="weight"),
    path("weight/add/", views.WeightCreateView.as_view(), name="weight_add"),
    path(
        "weight/delete/<int:pk>/",
        views.WeightDeleteView.as_view(),
        name="weight_delete",
    ),
]
