# Generated by Django 3.0.4 on 2020-03-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem_text', models.TextField()),
                ('poem_title', models.CharField(max_length=1000)),
            ],
        ),
    ]