# Generated by Django 3.0.9 on 2021-04-17 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_vmeste', '0002_auto_20210415_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoentryviewsstatisticsmonth',
            name='fk',
        ),
        migrations.DeleteModel(
            name='InfoEntryViewsStatistics',
        ),
        migrations.DeleteModel(
            name='InfoEntryViewsStatisticsMonth',
        ),
    ]
