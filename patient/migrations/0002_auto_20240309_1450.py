# Generated by Django 3.0.5 on 2024-03-09 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctorname',
        ),
    ]
