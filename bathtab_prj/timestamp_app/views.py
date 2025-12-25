from django.shortcuts import render


def pee(request):
    return render(request, "timestamp_app/pee.html")


def pill(request):
    return render(request, "timestamp_app/pill.html")
