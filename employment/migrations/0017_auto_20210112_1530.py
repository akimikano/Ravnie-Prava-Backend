# Generated by Django 3.0.9 on 2021-01-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0016_auto_20201204_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='audio_duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах'),
        ),
        migrations.AddField(
            model_name='empentryaudio',
            name='audio_duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах'),
        ),
        migrations.AddField(
            model_name='empentryaudio',
            name='audio_duration_kg',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах (кырг.)'),
        ),
        migrations.AddField(
            model_name='empentryphoto',
            name='audio_duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах'),
        ),
        migrations.AddField(
            model_name='empentryphoto',
            name='audio_duration_kg',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длительность аудио в секундах (кырг.)'),
        ),
    ]
