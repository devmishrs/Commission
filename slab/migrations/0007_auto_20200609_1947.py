# Generated by Django 3.0.7 on 2020-06-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0006_makecommission_tr_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributers',
            name='dist_name',
        ),
        migrations.AddField(
            model_name='distributers',
            name='dist_id',
            field=models.IntegerField(default=55711),
        ),
    ]