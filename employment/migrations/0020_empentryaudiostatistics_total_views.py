# Generated by Django 3.0.9 on 2021-04-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0019_auto_20210417_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='empentryaudiostatistics',
            name='total_views',
            field=models.PositiveIntegerField(default=0, verbose_name='Всего просмотров'),
        ),
    ]
