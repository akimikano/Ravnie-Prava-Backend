from django.db import models


class Section(models.Model):
    name = models.CharField('Название', max_length=250, default='')
    description = models.CharField('Краткая информация', max_length=250, default='')
    icon = models.FileField('Иконка', upload_to='main/icons', null=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name
