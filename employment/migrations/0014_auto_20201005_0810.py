# Generated by Django 3.0.9 on 2020-10-05 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0013_auto_20201005_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='others_set', to='employment.EmpHead', verbose_name='Глава'),
        ),
    ]
