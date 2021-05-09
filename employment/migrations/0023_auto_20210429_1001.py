# Generated by Django 3.0.9 on 2021-04-29 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0022_auto_20210420_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='empentryaudiofilestatistics',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_file_statistics', to='employment.Course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='empentryaudiofilestatistics',
            name='resume',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_file_statistics', to='employment.EmpEntryPhoto', verbose_name='Резюме'),
        ),
        migrations.AddField(
            model_name='empentryaudiolistenstatistics',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_listen_statistics', to='employment.Course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='empentryaudiolistenstatistics',
            name='resume',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_listen_statistics', to='employment.EmpEntryPhoto', verbose_name='Резюме'),
        ),
        migrations.AddField(
            model_name='empentryaudiostatistics',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_statistics', to='employment.Course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='empentryaudiostatistics',
            name='resume',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_statistics', to='employment.EmpEntryPhoto', verbose_name='Резюме'),
        ),
        migrations.AlterField(
            model_name='empentryaudiofilestatistics',
            name='emp_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_entry_file_statistics', to='employment.EmpEntryAudio', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='empentryaudiolistenstatistics',
            name='emp_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_entry_listen_statistics', to='employment.EmpEntryAudio', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='empentryaudiostatistics',
            name='emp_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_entry_statistics', to='employment.EmpEntryAudio', verbose_name='Статья'),
        ),
    ]