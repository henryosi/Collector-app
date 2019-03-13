from django.shortcuts import render
from django.http import HttpResponse
from.models import Auto


# Create your views here.
def home (request):
    return HttpResponse ('<h1>Hello Car Lovers</h1>')

def about (request):
    return render(request, 'about.html')

def autos_index(request):
    autos = Auto.objects.all()
    return render (request, 'autos/index.html', { 'autos': autos })

def autos_detail(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render (request, 'autos/index.html', { 'auto': auto })