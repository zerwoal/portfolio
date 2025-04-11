import markdown
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request,'skills.html',context={
        'index_page' : 'Compétences',
        'skills' : Skill.objects.all()
    })

def select_skill(request, slug):
    skill_object = get_object_or_404(Skill, slug=slug)
    # skill_object.markdowm_html = markdown.markdown(Skill.description)
    return render(request, 'skill.html', {
        'index_page' : skill_object.name,
        'skill' : skill_object,
    })