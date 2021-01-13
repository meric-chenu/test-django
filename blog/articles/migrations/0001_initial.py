# Generated by Django 3.1.2 on 2021-01-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('contenu', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
