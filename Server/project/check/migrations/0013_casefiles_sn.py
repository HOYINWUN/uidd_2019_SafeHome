# Generated by Django 2.2 on 2019-05-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0012_auto_20190509_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='casefiles',
            name='SN',
            field=models.CharField(default='000000000000', max_length=12),
        ),
    ]