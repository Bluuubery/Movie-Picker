# Generated by Django 3.2.13 on 2022-11-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='messsage',
            field=models.CharField(max_length=100, null=True),
        ),
    ]