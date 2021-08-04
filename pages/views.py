from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.(place that handles various web pages)

def home_view(request, *args, **kwargs):
    print("Request:", request, *args, **kwargs)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print("Request:", request, *args, **kwargs)
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    print("Request:", request, *args, **kwargs)
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    print("Request:", request, *args, **kwargs)
    return render(request, "social.html", {})