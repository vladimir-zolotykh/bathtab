from django.urls import path
from . import views

urlpatterns = [
    # path("", views.pee, name="pee"),
    path("", views.PeePooListView.as_view(), name="pee"),
    path("pee/add/", views.PeeCreateView.as_view(), name="pee_add"),
    path("pee/delete/<int:pk>/", views.PeeDeleteView.as_view(), name="pee_delete"),
    path("pee/<int:pk>/edit/", views.PeeUpdateView.as_view(), name="pee_edit"),
    path("poo/add/", views.PooCreateView.as_view(), name="poo_add"),
    path("poo/delete/<int:pk>/", views.PooDeleteView.as_view(), name="poo_delete"),
    path("poo/<int:pk>/edit/", views.PooUpdateView.as_view(), name="poo_edit"),
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
