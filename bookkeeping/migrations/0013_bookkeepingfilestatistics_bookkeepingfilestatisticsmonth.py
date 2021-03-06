# Generated by Django 3.0.9 on 2021-04-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0012_bookkeepingstatistics_bookkeepingstatisticsmonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookkeepingFileStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookkeeping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookkeeping_file_statistics', to='bookkeeping.BookKeeping', verbose_name='Полезная бухгалтерия')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
            },
        ),
        migrations.CreateModel(
            name='BookkeepingFileStatisticsMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статистика')),
                ('date', models.DateField(verbose_name='Дата')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний файла (ru)')),
                ('count_kg', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний файла (kg)')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookkeeping_file_statistics_months', to='bookkeeping.BookkeepingFileStatistics', verbose_name='Полезная бухгалтерия')),
            ],
            options={
                'verbose_name': 'Статистика скачиваний файла полезной бухгалтерии за месяц',
                'verbose_name_plural': 'Статистика скачиваний файла полезной бухгалтерии за месяц',
            },
        ),
    ]
