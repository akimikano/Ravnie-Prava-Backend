# Generated by Django 3.0.9 on 2020-08-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0007_auto_20200813_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='address',
            field=models.CharField(default='', max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='eduentry',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='eduhead',
            name='description',
            field=models.CharField(default='', max_length=250, verbose_name='Краткая информация'),
        ),
        migrations.AlterField(
            model_name='eduhead',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='address',
            field=models.CharField(default='', max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='ФИО'),
        ),
    ]