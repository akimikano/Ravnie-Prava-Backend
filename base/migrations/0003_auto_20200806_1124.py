# Generated by Django 3.0.9 on 2020-08-06 05:24

import audiofield.fields
import base.extra
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200805_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='file',
            field=base.extra.ContentTypeRestrictedFileField(null=True, upload_to='base/documents'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='audio_file',
            field=audiofield.fields.AudioField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='base/audio'),
        ),
    ]
