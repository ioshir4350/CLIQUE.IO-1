# Generated by Django 3.0.6 on 2020-06-06 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_remove_postmodel_application_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='application_deadline',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Application Deadline'),
        ),
    ]