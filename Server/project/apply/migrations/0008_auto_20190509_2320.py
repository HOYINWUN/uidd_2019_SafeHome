# Generated by Django 2.2 on 2019-05-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0007_auto_20190509_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='addressAlley',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressCounty',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressDistrict',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressFloor',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressLane',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressNumber',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressRoad',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='case',
            name='addressRoom',
            field=models.CharField(max_length=5),
        ),
    ]
