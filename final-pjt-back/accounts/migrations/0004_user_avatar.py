# Generated by Django 3.2.13 on 2022-11-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default_avatar.svg', null=True, upload_to=''),
        ),
    ]
