# Generated by Django 5.1.6 on 2025-03-30 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='languages', verbose_name='Illustration')),
            ],
            options={
                'verbose_name': 'Langage',
                'verbose_name_plural': 'Langages',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nom')),
                ('libraries', models.CharField(help_text='Séparez les librairies par des virgules', max_length=100, verbose_name='Librairies')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='skills', verbose_name='Illustration')),
                ('mastery_level', models.IntegerField(choices=[(1, 'Debutant'), (2, 'Intermediaire'), (3, 'Avance'), (4, 'Expert')], default=1, verbose_name='Niveau')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skills.language', verbose_name='Langage')),
            ],
            options={
                'verbose_name': 'Compétence',
                'verbose_name_plural': 'Compétences',
            },
        ),
    ]
