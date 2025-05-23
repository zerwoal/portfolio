# Generated by Django 5.1.6 on 2025-03-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nom')),
                ('image', models.ImageField(upload_to='database/projects/images', verbose_name='Image')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Sous-titre')),
                ('description', models.TextField(help_text='Utilisez Markdown', verbose_name='Description')),
                ('type', models.CharField(choices=[('url', 'URL'), ('file', 'Fichier')], max_length=40, verbose_name='Type')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
            },
        ),
    ]
