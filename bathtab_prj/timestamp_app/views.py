from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic import UpdateView
from .models import PillLog, PillNote

from .models import WeightLog, PeeLog, PooLog
from .forms import PillLogForm
from .forms import PeeLogForm, PooLogForm


class BaseLogUpdateView(UpdateView):
    template_name = "timestamp_app/log_edit.html"

    def get_success_url(self):
        return reverse_lazy("pee")


class PeePooListView(ListView):
    template_name = "timestamp_app/pee.html"
    context_object_name = "pee_logs"

    def get_queryset(self):
        return PeeLog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poo_logs"] = PooLog.objects.all()
        context["pee_form"] = PeeLogForm()
        context["poo_form"] = PooLogForm()
        return context


class PeeCreateView(CreateView):
    model = PeeLog
    form_class = PeeLogForm
    success_url = reverse_lazy("pee")


class PooCreateView(CreateView):
    model = PooLog
    form_class = PooLogForm
    success_url = reverse_lazy("pee")


# def pee(request):
#     return render(request, "timestamp_app/pee.html")


# def pill(request):
#     return render(request, "timestamp_app/pill.html")


class PeeDeleteView(DeleteView):
    model = PeeLog
    success_url = reverse_lazy("pee")


class PooDeleteView(DeleteView):
    model = PooLog
    success_url = reverse_lazy("pee")


class PeeUpdateView(BaseLogUpdateView):
    model = PeeLog
    form_class = PeeLogForm


class PooUpdateView(BaseLogUpdateView):
    model = PooLog
    form_class = PooLogForm


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


class PillUpdateView(UpdateView):
    model = PillLog
    form_class = PillLogForm
    template_name = "timestamp_app/pill_edit.html"
    success_url = reverse_lazy("pill")
