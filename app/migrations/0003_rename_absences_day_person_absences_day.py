# Generated by Django 4.2.4 on 2023-08-06 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_rewrd_details_person_rwrd_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='absences_Day',
            new_name='absences_day',
        ),
    ]
