# Generated by Django 4.0.6 on 2024-04-21 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_remove_course_course_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scientific_area',
            name='presentation',
        ),
    ]
