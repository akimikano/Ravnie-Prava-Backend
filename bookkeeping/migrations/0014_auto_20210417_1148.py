# Generated by Django 3.0.9 on 2021-04-17 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0013_bookkeepingfilestatistics_bookkeepingfilestatisticsmonth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookkeepingfilestatistics',
            options={'verbose_name': 'Статистика скачиваний файла полезной бухгалтерии', 'verbose_name_plural': 'Статистика скачиваний файлов полезной бухгалтерии'},
        ),
        migrations.AlterModelOptions(
            name='bookkeepingstatistics',
            options={'verbose_name': 'Статистика просмотров статьи', 'verbose_name_plural': 'Статистика просмотров статьи'},
        ),
    ]
