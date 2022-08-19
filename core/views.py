from django.shortcuts import render
from time import strftime
from .Facts import random_facts

def index(request):
    a = strftime('%A %B %d %Y')
    b = strftime('%I:%M %p')
    context = {
        'title':'103 cool facts',
        'date':a,
        'time':b,
        'fact':random_facts()
        }
    return render(request, 'index.html', context)

# Create your views here.