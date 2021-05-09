# Generated by Django 3.0.9 on 2021-04-17 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0015_eduentrystatistics_eduentrystatisticsmonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduEntryFileStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='edu_entry_file_statistics', to='edu.EduEntry', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Статистика скачивания файлов статьи',
                'verbose_name_plural': 'Статистика скачиваний файлов статей',
            },
        ),
        migrations.AlterModelOptions(
            name='eduentrystatistics',
            options={'verbose_name': 'Статистика просмотра статьи', 'verbose_name_plural': 'Статистика просмотра статей'},
        ),
        migrations.CreateModel(
            name='EduEntryFileStatisticsMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статистика')),
                ('date', models.DateField(verbose_name='Дата')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний файла (ru)')),
                ('count_kg', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний файла (kg)')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu_entry_file_statistics_months', to='edu.EduEntryFileStatistics', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Статистика статьи за месяц',
                'verbose_name_plural': 'Статистика статьи за месяц',
            },
        ),
    ]