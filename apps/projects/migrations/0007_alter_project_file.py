# Generated by Django 5.1.6 on 2025-04-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='projects/files', verbose_name='Fichier'),
        ),
    ]
