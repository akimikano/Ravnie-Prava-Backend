# Generated by Django 3.0.9 on 2021-04-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20210418_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entryfilestatistics',
            options={'verbose_name': 'Статистика скачиваний файла статьи', 'verbose_name_plural': 'Статистика скачиваний файлов статей'},
        ),
        migrations.AlterModelOptions(
            name='entrystatistics',
            options={'verbose_name': 'Статистика просмотров статьи', 'verbose_name_plural': 'Статистика просмотров статей'},
        ),
        migrations.AlterField(
            model_name='entrylistenstatisticsmonth',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество прослушиваний (ru)'),
        ),
        migrations.AlterField(
            model_name='entrylistenstatisticsmonth',
            name='count_kg',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество прослушиваний (kg)'),
        ),
    ]
