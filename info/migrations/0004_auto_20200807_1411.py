# Generated by Django 3.0.9 on 2020-08-07 08:11

import audiofield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20200807_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='audio_file',
            field=audiofield.fields.AudioField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='info/'),
        ),
        migrations.AlterField(
            model_name='new',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads/images/', verbose_name='Фото'),
        ),
    ]