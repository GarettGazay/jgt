# Generated by Django 2.1.1 on 2018-09-27 00:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20180926_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcsv',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]