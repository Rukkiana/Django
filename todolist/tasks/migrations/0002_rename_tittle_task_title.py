# Generated by Django 5.0.8 on 2024-08-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tittle',
            new_name='title',
        ),
    ]
