# Generated by Django 3.0.9 on 2020-11-11 10:14

import base.extra
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_auto_20200904_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduentry',
            name='audio_file_kg',
            field=models.FileField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='edu/audio', verbose_name='Аудио (кырг.)'),
        ),
        migrations.AddField(
            model_name='eduentry',
            name='file_kg',
            field=base.extra.ContentTypeRestrictedFileField(blank=True, help_text='Допустимый формат - .pdf', null=True, upload_to='edu/documents', verbose_name='Файл (кырг.)'),
        ),
    ]