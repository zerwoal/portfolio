from django.shortcuts import render, get_object_or_404
from .models import *
import markdown


projects = Project.objects.all()

# Create your views here.
def index(request):
    return render(request, 'projects.html', context={
        'index_page' : "Projets",
        'projects' : Project.objects.all(),
    })

def select_project(request, slug):
    project_object = get_object_or_404(Project, slug=slug)
    project_object.markdown_html = markdown.markdown(project_object.description)

    return render(request, 'project.html', context={
        'index_page' : project_object.name,
        'project' : project_object,
    })