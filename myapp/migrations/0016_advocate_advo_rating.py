# Generated by Django 4.1.2 on 2024-03-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='advo_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
