# Generated by Django 3.0.9 on 2020-11-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20201130_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoentry',
            name='title',
        ),
    ]