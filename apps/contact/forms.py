from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom' ,widget=forms.TextInput(attrs={'placeholder' : 'Nom'}), required=True)
    subject = forms.CharField(label="Objet", widget=forms.TextInput(attrs={'placeholder' : 'Objet'}), required=True)
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'placeholder' : 'Adresse email'}),
        validators=[EmailValidator()],
        required=True,
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea
        (attrs={'placeholder' : 'Votre message'}),
        required=True
    )
