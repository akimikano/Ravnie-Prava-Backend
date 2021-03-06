# Generated by Django 3.0.9 on 2021-04-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0011_auto_20210112_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookkeepingStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookkeeping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookkeeping_statistics', to='bookkeeping.BookKeeping', verbose_name='Полезная бухгалтерия')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
            },
        ),
        migrations.CreateModel(
            name='BookkeepingStatisticsMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статистика')),
                ('date', models.DateField(verbose_name='Дата')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookkeeping_statistics_months', to='bookkeeping.BookkeepingStatistics', verbose_name='Полезная бухгалтерия')),
            ],
            options={
                'verbose_name': 'Статистика полезной бухгалтерии за месяц',
                'verbose_name_plural': 'Статистика полезной бухгалтерии за месяц',
            },
        ),
    ]
