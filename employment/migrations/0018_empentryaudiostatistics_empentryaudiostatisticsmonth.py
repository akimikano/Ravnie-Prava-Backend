# Generated by Django 3.0.9 on 2021-04-17 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0017_auto_20210112_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpEntryAudioStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emp_entry_statistics', to='employment.EmpEntryAudio', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
            },
        ),
        migrations.CreateModel(
            name='EmpEntryAudioStatisticsMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статистика')),
                ('date', models.DateField(verbose_name='Дата')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_entry_statistics_months', to='employment.EmpEntryAudioStatistics', verbose_name='')),
            ],
            options={
                'verbose_name': 'Статистика статьи за месяц',
                'verbose_name_plural': 'Статистика статьи за месяц',
            },
        ),
    ]
