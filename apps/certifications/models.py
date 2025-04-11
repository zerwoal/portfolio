from django.db import models
from django.urls import reverse
from apps.skills.models import Language

# Create your models here.

class Certification(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    organism = models.CharField(max_length=100, verbose_name='Organisme')
    duration = models.IntegerField(verbose_name='Durée')
    duration_measure = models.CharField(verbose_name="Unité de mesure", default='Jour', max_length=120, choices={
        "heures": "heures",
        "jours": "jours",
        "mois": "mois",
        "ans": "ans",
        "trimestres": "trimestres",
    })
    # mastery = models.CharField(max_length=100, verbose_name='Maîtrise', choices={
    #         1 : 'Debutant',
    #         2 : 'Intermediaire',
    #         3 : 'Avance',
    #         4 : 'Expert',
    #         }   )
    date = models.DateField(verbose_name="Date d'obention")
    language = models.ForeignKey(Language, models.SET_NULL, null=True)
    description = models.TextField(help_text='Utilisez Markdown', verbose_name='Description')
    image = models.ImageField(upload_to='certifications', null=True, blank=True, verbose_name='Image')
    slug = models.SlugField(unique=True, max_length=50, verbose_name='Slug')

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.name