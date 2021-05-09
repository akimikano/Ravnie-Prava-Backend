# Generated by Django 3.0.9 on 2020-08-05 10:22

import audiofield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Краткая информация')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heads_set', to='main.Section', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Глава',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('audio_file', audiofield.fields.AudioField(blank=True, help_text='Допустимые форматы - .mp3, .wav, .ogg', null=True, upload_to='base/')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_set', to='base.Head', verbose_name='Глава')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
    ]