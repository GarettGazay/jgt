# Generated by Django 2.0.5 on 2018-08-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0041_auto_20180821_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbasic',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=1),
        ),
    ]