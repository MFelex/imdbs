# Generated by Django 2.2.4 on 2019-08-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='crew_avatar', verbose_name='avatar'),
        ),
    ]
