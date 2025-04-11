from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'experiences.html',{
        'index_page' : 'Experiences',
        'experiences' : Experience.objects.all(),
        'opinions' : Opinion.objects.all()
    })