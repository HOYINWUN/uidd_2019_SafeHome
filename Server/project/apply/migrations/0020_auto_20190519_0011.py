# Generated by Django 2.2 on 2019-05-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0019_case_buildingfloors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='lineID',
            field=models.CharField(max_length=100),
        ),
    ]
