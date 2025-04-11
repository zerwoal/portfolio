from django.db import models
from django.urls import reverse

# Create your models here.
class Language(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    name = models.CharField("Nom",max_length=100)
    slug = models.SlugField("Slug", unique=True, max_length=50)
    image = models.ImageField("Illustration", upload_to='languages', null=True, blank=True)

    class Meta:
        verbose_name = "Langage"
        verbose_name_plural = "Langages"

    def __str__(self):
        return self.name

class Skill(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

    mastery ={
        1 : 'Debutant',
        2 : 'Intermediaire',
        3 : 'Avance',
        4 : 'Expert',
        }   

    name = models.CharField("Nom",max_length=100, default="")
    language = models.ForeignKey("Language", verbose_name="Langage", on_delete=models.SET_NULL, null=True)
    libraries = models.CharField("Librairies", help_text="Séparez les librairies par des virgules", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Illustration", upload_to='skills', null=True, blank=True)
    mastery_level = models.IntegerField("Niveau",choices=mastery, default=1)
    slug = models.SlugField("Slug", unique=True, max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def get_absolute_url(self):
        return reverse("skill", kwargs={'slug': self.slug})