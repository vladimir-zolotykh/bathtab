from django.urls import path
from . import views

urlpatterns = [
    path("", views.pee, name="pee"),
    path("pill/", views.PillListView.as_view(), name="pill"),
    path("pill/add/", views.PillCreateView.as_view(), name="pill_add"),
    path(
        "pill/delete/<int:pk>/",
        views.PillDeleteView.as_view(),
        name="pill_delete",
    ),
    path(
        "pill/note/delete/<int:pk>/",
        views.PillNoteDeleteView.as_view(),
        name="pill_note_delete",
    ),
    path("weight/", views.WeightListView.as_view(), name="weight"),
    path("weight/add/", views.WeightCreateView.as_view(), name="weight_add"),
    path(
        "weight/delete/<int:pk>/",
        views.WeightDeleteView.as_view(),
        name="weight_delete",
    ),
    path("pill/<int:pk>/edit/", views.PillUpdateView.as_view(), name="pill_edit"),
]
