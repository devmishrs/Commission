# Generated by Django 3.0.7 on 2020-06-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0003_setcommission'),
    ]

    operations = [
        migrations.AddField(
            model_name='setcommission',
            name='share',
            field=models.FloatField(default=0.0),
        ),
    ]
