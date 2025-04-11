from django.contrib import admin
from apps.about.models import *
from apps.contact.models import *
from apps.experiences.models import *
from apps.main.models import *
from apps.projects.models import *
from apps.skills.models import *

# Register your models here.
models_to_register = [
    Skill, Language, Experience, Opinion, Project
]

for model in models_to_register:
    admin.site.register(model)