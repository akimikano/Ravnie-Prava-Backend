# Generated by Django 3.0.9 on 2020-08-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='icon',
            field=models.FileField(null=True, upload_to='uploads/main/icons', verbose_name='Иконка'),
        ),
    ]