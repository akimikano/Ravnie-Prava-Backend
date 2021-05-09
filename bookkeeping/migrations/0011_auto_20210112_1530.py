# Generated by Django 3.0.9 on 2021-01-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0010_bookkeeping_audio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookkeeping',
            name='audio_duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах'),
        ),
        migrations.AddField(
            model_name='bookkeeping',
            name='audio_duration_kg',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах (кырг.)'),
        ),
    ]
