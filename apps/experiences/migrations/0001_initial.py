# Generated by Django 5.1.6 on 2025-04-01 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nom')),
                ('location', models.CharField(max_length=120, verbose_name='Localisation')),
                ('logo', models.ImageField(upload_to='experiences', verbose_name='Illustration')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('opinion_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiences.experience')),
            ],
            options={
                'verbose_name': 'Opinion',
                'verbose_name_plural': 'Opinions',
            },
        ),
    ]
