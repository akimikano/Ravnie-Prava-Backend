# Generated by Django 3.0.9 on 2020-08-06 07:50

import base.extra
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200806_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='file',
            field=base.extra.ContentTypeRestrictedFileField(help_text='Допустимый формат - .pdf', null=True, upload_to='base/documents', verbose_name='Файл'),
        ),
    ]
