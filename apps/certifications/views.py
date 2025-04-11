from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'certifications.html',context={
        'index_page' : 'Certifications',
    })