# Generated by Django 2.1.1 on 2018-09-08 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0053_auto_20180907_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formbasic',
            name='dl_user',
        ),
        migrations.RemoveField(
            model_name='reocurring',
            name='dl_user',
        ),
    ]
