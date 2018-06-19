from django.shortcuts import render, HttpResponse

# Create your views here.

"""
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/
"""


def home(request):
    return HttpResponse("Inicio")


def about(request):
    return HttpResponse("About")


def services(request):
    return HttpResponse("Services")


def store(request):
    return HttpResponse("Visítanos")


def contact(request):
    return HttpResponse("Contacto")


def blog(request):
    return HttpResponse("Blog")


def sample(request):
    return HttpResponse("Sample")
