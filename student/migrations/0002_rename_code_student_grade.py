# Generated by Django 4.1.4 on 2022-12-23 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='code',
            new_name='grade',
        ),
    ]