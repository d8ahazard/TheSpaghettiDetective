# Generated by Django 2.1.7 on 2019-11-04 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20191103_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='printer',
            options={'default_manager_name': 'objects'},
        ),
    ]