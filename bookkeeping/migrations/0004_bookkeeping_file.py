# Generated by Django 3.0.9 on 2020-08-07 05:29

import base.extra
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0003_bookkeeping_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookkeeping',
            name='file',
            field=base.extra.ContentTypeRestrictedFileField(help_text='Допустимый формат - .pdf', null=True, upload_to='base/documents', verbose_name='Файл'),
        ),
    ]
