# Generated by Django 2.1.5 on 2023-03-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=128, unique=True)),
                ('date', models.CharField(max_length=128, unique=True)),
                ('body', models.CharField(max_length=50000, unique=True)),
            ],
        ),
    ]
