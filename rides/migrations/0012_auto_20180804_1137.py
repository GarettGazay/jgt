# Generated by Django 2.0.5 on 2018-08-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0011_auto_20180803_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formbasic',
            name='end_address',
        ),
        migrations.RemoveField(
            model_name='formbasic',
            name='start_address',
        ),
        migrations.AddField(
            model_name='formbasic',
            name='pickup_address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='formbasic',
            name='pickup_time',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='formbasic',
            name='return_address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='formbasic',
            name='return_time',
            field=models.CharField(default='', max_length=3),
        ),
    ]