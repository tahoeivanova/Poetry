# Generated by Django 3.0.4 on 2020-04-19 15:59

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='poem',
            managers=[
                ('pushkin', django.db.models.manager.Manager()),
            ],
        ),
    ]
