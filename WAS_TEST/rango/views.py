from django.shortcuts import render
from django.http import HttpResponse
from rango.models import News

def index(request):

    category_list = News.objects.all
    context_dict = {}
    context_dict['categories'] = category_list



    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    response = HttpResponse()
    response.write("<p>about page</p>")

    return response
