from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def index_view(request):
    return HttpResponse('<h1>here is home page</h1>')

def about_view(request):
    return HttpResponse('<h1>here is about page</h1>')

def contact_view(request):
    return HttpResponse('<h1>here is contact page</h1>')