# Generated by Django 3.0.9 on 2020-12-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0009_auto_20201111_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookkeeping',
            name='audio_image',
            field=models.FileField(blank=True, null=True, upload_to='bookkeeping/images', verbose_name='Фото для аудио'),
        ),
    ]
