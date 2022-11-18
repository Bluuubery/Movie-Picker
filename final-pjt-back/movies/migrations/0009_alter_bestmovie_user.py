# Generated by Django 3.2.13 on 2022-11-18 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0008_auto_20221118_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestmovie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='best_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]