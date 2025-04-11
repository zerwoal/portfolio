"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from source.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('', include('apps.main.urls')),
    path('contact/', include('apps.contact.urls')),
    path('experiences/', include('apps.experiences.urls')),
    path('footer/', include('apps.footer_part.urls')),
    path('projects/', include('apps.projects.urls')),
    path('skills/', include('apps.skills.urls')),
    path('certifications', include('apps.certifications.urls')),
    path('admin/', admin.site.urls),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

