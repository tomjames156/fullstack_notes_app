# Generated by Django 4.2.2 on 2023-06-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='note_heading',
        ),
    ]
