# Generated by Django 5.1.6 on 2025-04-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_opinion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='website',
            field=models.URLField(null=True, verbose_name='Site web'),
        ),
    ]
