# Generated by Django 2.1.3 on 2018-11-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qytcloud', '0004_auto_20181123_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmdb',
            name='vm_status1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
