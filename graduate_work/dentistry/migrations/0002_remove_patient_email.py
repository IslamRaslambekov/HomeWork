# Generated by Django 4.0.4 on 2022-04-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]