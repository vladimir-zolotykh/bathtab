from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import PillLog, PillNote

from .models import WeightLog
from .forms import PillLogForm


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


class PillListView(ListView):
    model = PillLog
    template_name = "timestamp_app/pill.html"
    context_object_name = "pill_logs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = PillNote.objects.all()
        context["form"] = PillLogForm()
        return context


class PillCreateView(CreateView):
    model = PillLog
    form_class = PillLogForm
    success_url = reverse_lazy("pill")


class PillDeleteView(DeleteView):
    model = PillLog
    success_url = reverse_lazy("pill")


class PillNoteDeleteView(DeleteView):
    model = PillNote
    success_url = reverse_lazy("pill")
