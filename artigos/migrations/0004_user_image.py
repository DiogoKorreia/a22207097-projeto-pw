# Generated by Django 4.0.6 on 2024-04-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_topic_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='artigos/images'),
        ),
    ]
