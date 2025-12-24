from django.shortcuts import render


def home(request):
    return render(request, "timestamp_app/home.html")
