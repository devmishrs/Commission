# Generated by Django 3.0.7 on 2020-06-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0007_auto_20200609_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makecommission',
            name='distributer',
        ),
        migrations.AddField(
            model_name='makecommission',
            name='dist_id',
            field=models.IntegerField(default=44810),
        ),
        migrations.AlterField(
            model_name='distributers',
            name='dist_id',
            field=models.IntegerField(default=68295),
        ),
    ]
