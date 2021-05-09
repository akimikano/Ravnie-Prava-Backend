# Generated by Django 3.0.9 on 2020-08-13 08:37

import base.extra
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0007_auto_20200812_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='file',
            field=base.extra.ContentTypeRestrictedFileField(blank=True, help_text='Допустимый формат - .pdf', null=True, upload_to='employment/documents', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='empentryaudio',
            name='file',
            field=base.extra.ContentTypeRestrictedFileField(blank=True, help_text='Допустимый формат - .pdf', null=True, upload_to='employment/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='course',
            name='audio_file',
            field=models.FileField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='employment/audio', verbose_name='Аудио'),
        ),
        migrations.AlterField(
            model_name='empentryaudio',
            name='audio_file',
            field=models.FileField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='employment/audio', verbose_name='Аудио'),
        ),
        migrations.AlterField(
            model_name='empentryphoto',
            name='audio_file',
            field=models.FileField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='employment/audio', verbose_name='Аудио'),
        ),
        migrations.AlterField(
            model_name='empentryphoto',
            name='photo',
            field=models.FileField(blank=True, upload_to='employment/photos', verbose_name='Файл'),
        ),
    ]
