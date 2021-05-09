# Generated by Django 3.0.9 on 2021-04-29 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0020_auto_20210423_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduentryfilestatistics',
            name='dept',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_file_statistics', to='edu.Dept', verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='eduentrylistenstatistics',
            name='dept',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_listen_statistics', to='edu.Dept', verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='eduentrystatistics',
            name='dept',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_statistics', to='edu.Dept', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='eduentrystatistics',
            name='edu_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edu_entry_statistics', to='edu.EduEntry', verbose_name='Статья'),
        ),
    ]
