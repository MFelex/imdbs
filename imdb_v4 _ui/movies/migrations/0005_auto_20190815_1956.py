# Generated by Django 2.2.4 on 2019-08-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20190815_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/movies/user_deafult.png', upload_to='crew_avatar', verbose_name='avatar'),
        ),
    ]
