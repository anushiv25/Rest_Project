# Generated by Django 2.2.2 on 2019-06-25 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
    ]
