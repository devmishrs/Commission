# Generated by Django 3.0.7 on 2020-06-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0009_auto_20200610_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='makecommission',
            name='d_share',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='makecommission',
            name='m_share',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='makecommission',
            name='z_share',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='distributers',
            name='dist_id',
            field=models.IntegerField(default=45943),
        ),
        migrations.AlterField(
            model_name='makecommission',
            name='dist_id',
            field=models.IntegerField(default=74808, unique=True),
        ),
    ]