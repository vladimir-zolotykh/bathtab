from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .models import WeightLog


def pee(request):
    return render(request, "timestamp_app/pee.html")


def pill(request):
    return render(request, "timestamp_app/pill.html")


class WeightListView(ListView):
    model = WeightLog
    template_name = "timestamp_app/weight.html"
    context_object_name = "weights"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last = WeightLog.objects.first()
        context["last_weight"] = last.weight if last else ""
        return context


class WeightCreateView(CreateView):
    model = WeightLog
    fields = ["weight"]
    success_url = reverse_lazy("weight")


class WeightDeleteView(DeleteView):
    model = WeightLog
    success_url = reverse_lazy("weight")
