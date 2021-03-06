# Generated by Django 2.2.3 on 2019-08-05 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='moderated_operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='moderated_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='moderated_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='moderated time'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'new comment'), (1, 'approved'), (2, 'rejected')], default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
