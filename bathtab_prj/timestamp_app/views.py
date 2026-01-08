from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic import UpdateView
from .models import PillLog, PillNote

from .models import WeightLog, PeeLog, PooLog
from .forms import PillLogForm
from .forms import PeeLogForm, PooLogForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404


class BaseLogUpdateView(UpdateView):
    template_name = "timestamp_app/log_edit.html"

    def get_success_url(self):
        return reverse_lazy("pee")


class BaseLogDeleteView(DeleteView):
    template_name = "timestamp_app/confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            messages.info(request, "This item has already been deleted.")
            return redirect(self.get_success_url())

    def get_success_url(self):
        # 1) Explicit redirect target
        if next_url := self.request.GET.get("next"):
            return next_url

        # 2) Referrer, if it is not the delete page itself
        referer = self.request.META.get("HTTP_REFERER")
        if referer and not referer.endswith(self.request.path):
            return referer

        # 3) Safe fallback
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


class PeeDeleteView(BaseLogDeleteView):
    model = PeeLog


class PooDeleteView(BaseLogDeleteView):
    model = PooLog


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


class WeightDeleteView(BaseLogDeleteView):
    model = WeightLog


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
    template_name = "timestamp_app/pill.html"
    success_url = reverse_lazy("pill")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pill_logs"] = PillLog.objects.all()
        context["notes"] = PillNote.objects.all()
        return context


class PillDeleteView(BaseLogDeleteView):
    model = PillLog


class PillNoteDeleteView(BaseLogDeleteView):
    model = PillNote


class PillUpdateView(UpdateView):
    model = PillLog
    form_class = PillLogForm
    template_name = "timestamp_app/pill_edit.html"
    success_url = reverse_lazy("pill")
