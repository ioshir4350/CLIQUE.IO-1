# Generated by Django 3.0.6 on 2020-06-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize_main', '0002_account_show_to_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(default='No Bio At The Moment'),
        ),
    ]
