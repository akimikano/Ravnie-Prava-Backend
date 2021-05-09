# Generated by Django 3.0.9 on 2020-11-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20201130_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoentry',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='infoentry',
            name='photo',
            field=models.ImageField(null=True, upload_to='info/images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='infoentry',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='infoentry',
            name='title',
            field=models.CharField(default='', max_length=250, verbose_name='Заголовок'),
        ),
    ]
