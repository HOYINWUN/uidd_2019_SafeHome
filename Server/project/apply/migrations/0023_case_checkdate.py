# Generated by Django 2.2 on 2019-05-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0022_auto_20190528_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='checkDate',
            field=models.CharField(default='undefined', max_length=60),
        ),
    ]