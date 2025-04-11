from django.core.mail import send_mail
from django.db.models.sql.query import Col
from django.shortcuts import render, redirect
from source import settings
from django.conf import settings
from apps.experiences.models import *

from apps.contact.forms import *
# Create your views here.

sent = False

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #récupération des données
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #envoi de l'email
            send_mail(
                subject="Contact portfolio",
                message= f"""

                    Bonjour,

                    Vous avez un nouveau message de {name} ({email}).


                    Voici son message : 
    - {subject}
{message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            #email de test
            send_mail(
                subject="Confirmation de votre message - Polleux",
                message=f"""
    Bonjour {name},

Nous avons bien reçu votre message, nous vous contacterons sous peu.

Cordialement

    Polleux Axel

                """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
        sent = True
        return redirect('contact/thanks')
    else:
        form = ContactForm()


# defining objects
    # experiences = Experience.objects.filter(is_priority=True)

    # defining variables

    return render(request,'index.html',context= {
        'index_page' : 'Accueil',
        'experiences' : Experience.objects.filter(is_priority=True),
        'contact_form' : ContactForm,
        },)
