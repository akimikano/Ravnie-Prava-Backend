# Generated by Django 3.0.9 on 2020-09-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0009_auto_20200904_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dept',
            name='type',
        ),
        migrations.RemoveField(
            model_name='eduentry',
            name='type',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='type',
        ),
        migrations.AddField(
            model_name='eduhead',
            name='type',
            field=models.CharField(choices=[('audio', 'Аудиозапись'), ('lawyer', 'Юрист')], default='audio', max_length=20, verbose_name='Тип'),
        ),
    ]