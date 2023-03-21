from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = HttpResponse()
    response.write("<p>Rango says he there Partner</p>")
    response.write("<p>WAS<p>")
    return response

def about(request):
    response = HttpResponse()
    response.write("<p>about page</p>")

    return response