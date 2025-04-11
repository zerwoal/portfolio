from django.shortcuts import render
from apps.main.views import *

# Create your views here.
def thanks(request):
        return render(request, 'thanks.html', {
            'index_page': 'Merci',
        })