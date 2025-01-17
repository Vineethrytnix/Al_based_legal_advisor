# Generated by Django 4.1.2 on 2024-03-02 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_case_details_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.CharField(max_length=100)),
                ('utype', models.CharField(max_length=100)),
                ('Advo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.advocate')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userregistration')),
            ],
        ),
    ]
