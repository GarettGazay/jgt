# Generated by Django 2.1.1 on 2018-09-20 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chooser', '0002_auto_20180919_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reocurring',
            name='author',
        ),
        migrations.DeleteModel(
            name='Reocurring',
        ),
    ]