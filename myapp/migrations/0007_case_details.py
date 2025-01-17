# Generated by Django 4.1.3 on 2023-06-22 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_case_request_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('desc', models.CharField(max_length=100, null=True)),
                ('fees', models.CharField(max_length=100, null=True)),
                ('advocate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.advocate')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.userregistration')),
            ],
        ),
    ]
