# Generated by Django 3.0.9 on 2020-09-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0008_auto_20200814_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='type',
            field=models.CharField(default='Отдел', max_length=20, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='eduentry',
            name='type',
            field=models.CharField(default='Аудиозапись', max_length=20, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='type',
            field=models.CharField(default='Юрист', max_length=20, verbose_name='Тип'),
        ),
    ]