from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    name = models.CharField("Nom",max_length=40)
    image = models.ImageField("Image", upload_to='projects')
    subtitle = models.CharField("Sous-titre",max_length=100)
    description = models.TextField("Description", help_text="Utilisez Markdown")
    type = models.CharField("Type",max_length=40, choices={
        "url" : "URL",
        "file" : "Fichier",
    })

    url = models.URLField("URL", blank=True, null=True)
    file = models.FileField("Fichier", upload_to='projects/files', blank=True, null=True)

    slug = models.SlugField("Slug", unique=True, max_length=50)

    def get_absolute_url(self):
        return reverse("project", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.name