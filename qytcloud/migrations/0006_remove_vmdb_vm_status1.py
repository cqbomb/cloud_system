# Generated by Django 2.1.3 on 2018-11-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qytcloud', '0005_vmdb_vm_status1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmdb',
            name='vm_status1',
        ),
    ]
