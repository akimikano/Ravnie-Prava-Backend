# Generated by Django 3.0.9 on 2020-08-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookkeeping',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Название'),
        ),
    ]