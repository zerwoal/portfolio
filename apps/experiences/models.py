from django.db import models
from django.urls import reverse

# Create your models here.
class Experience(models.Model):
    name = models.CharField("Nom", max_length=120)
    location = models.CharField("Localisation", max_length=120)
    logo = models.ImageField("Illustration", upload_to='experiences')
    description = models.TextField("Description")
    website = models.URLField('Site web', blank=True, null=True)
    is_priority = models.BooleanField("Afficher sur la page de garde")
    slug = models.SlugField("Slug", unique=True)
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("experience", kwargs={"slug": self.slug})    


class Opinion(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    name = models.CharField("Nom", max_length=120)
    role = models.CharField("Fonction", max_length=120, default='Employé')
    description = models.TextField("Description")
    image = models.ImageField("Illustration", upload_to='opinions', blank=True, null=True)

    class Meta:
        verbose_name = "Opinion"
        verbose_name_plural = "Opinions"

    def __str__(self):
        return self.name