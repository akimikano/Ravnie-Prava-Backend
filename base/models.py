from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.extra import ContentTypeRestrictedFileField
from main.models import Section


class Head(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='heads_set',
                                verbose_name='Раздел')
    name = models.CharField('Название', max_length=250, default='')
    description = models.CharField('Краткая информация', max_length=250, default='')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.name


class Entry(models.Model):
    head = models.ForeignKey('Head', on_delete=models.CASCADE, related_name='articles_set',
                             verbose_name='Глава')
    name = models.CharField('Название', max_length=250, default='')
    file = ContentTypeRestrictedFileField(upload_to='base/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='base/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='base/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='base/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='base/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name


class EntryStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотров статьи'
        verbose_name_plural = 'Статистика просмотров статей'

    entry = models.OneToOneField(Entry, verbose_name='Статья', related_name='entry_statistics',
                                       on_delete=models.CASCADE)
    total_views = models.PositiveIntegerField('Всего просмотров', default=0)

    def __str__(self):
        return f'Статистика просмотров статьи "{self.entry.name}"'


class EntryStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика статьи за месяц'
        verbose_name_plural = 'Статистика статьи за месяц'

    fk = models.ForeignKey(EntryStatistics, verbose_name='Статистика статьи',
                           related_name='entry_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.name


class EntryFileStatistics(models.Model):
    class Meta:
        verbose_name = 'Статистика скачиваний файла статьи'
        verbose_name_plural = 'Статистика скачиваний файлов статей'

    entry = models.OneToOneField(Entry, verbose_name='Статья', related_name='entry_file_statistics', on_delete=models.CASCADE)

    def __str__(self):
        return f'Статистика скачиваний файла статьи "{self.entry.name}"'


class EntryFileStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла за месяц'
        verbose_name_plural = 'Статистика скачиваний файла за месяц'

    fk = models.ForeignKey(EntryFileStatistics, verbose_name='Статистика статьи',
                           related_name='entry_file_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество скачиваний файла (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество скачиваний файла (kg)', default=0)

    def __str__(self):
        return self.name


class EntryListenStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи'
        verbose_name_plural = 'Статистика прослушиваний статей'

    entry = models.OneToOneField(Entry, verbose_name='Статья', related_name='entry_listen_statistics',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'Статистика прослушиваний статьи "{self.entry.name}"'


@receiver(post_save, sender=Entry)
def create_statistics(sender, instance, created, **kwargs):
    if created:
        EntryStatistics.objects.create(entry=instance)
        EntryFileStatistics.objects.create(entry=instance)
        EntryListenStatistics.objects.create(entry=instance)


class EntryListenStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла за месяц'
        verbose_name_plural = 'Статистика скачиваний файла за месяц'

    fk = models.ForeignKey(EntryListenStatistics, verbose_name='Статистика статьи',
                           related_name='entry_listen_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество прослушиваний (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество прослушиваний (kg)', default=0)

    def __str__(self):
        return self.name