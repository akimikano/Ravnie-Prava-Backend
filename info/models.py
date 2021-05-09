from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.extra import ContentTypeRestrictedFileField
from main.models import Section


TYPE_CHOICES = (
    ('news', 'Новости'),
    ('sub', 'Подглавы'),
)


class InfoHead(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE,
                                related_name='infoheads_set', verbose_name='Глава')
    name = models.CharField('Название', max_length=250, default='')
    description = models.CharField('Краткая информация', max_length=250, default='')
    type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES, default='news')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.name


class New(models.Model):
    head = models.ForeignKey('InfoHead', on_delete=models.CASCADE, related_name='news_set', verbose_name='Глава')
    title = models.CharField('Заголовок', max_length=250, default='')
    text = models.TextField('Текст')
    photo = models.ImageField('Фото', upload_to='info/images/', null=True)
    date = models.DateField(auto_now_add=True, blank=True)
    file = ContentTypeRestrictedFileField(upload_to='info/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='info/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='info/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='info/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='info/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class InfoSubhead(models.Model):
    name = models.CharField('Название', max_length=250, default='')
    head = models.ForeignKey('InfoHead', on_delete=models.CASCADE,
                             related_name='infosubheads_set', verbose_name='Глава')

    class Meta:
        verbose_name = 'Подглава'
        verbose_name_plural = 'Подглавы'

    def __str__(self):
        return self.name


class InfoEntry(models.Model):
    subhead = models.ForeignKey('InfoSubhead', on_delete=models.CASCADE,
                                related_name='infoentries_set', verbose_name='Подглава')
    name = models.CharField('Статья', max_length=250, default='')
    text = models.TextField('Текст', default='')
    photo = models.ImageField('Фото', upload_to='info/images/', null=True)
    date = models.DateField(null=True, auto_now_add=True, blank=True)
    file = ContentTypeRestrictedFileField(upload_to='info/documents', null=True, content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='info/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='info/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='info/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='info/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name


class InfoEntryStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотров статьи'
        verbose_name_plural = 'Статистика просмотров статей'

    info_entry = models.OneToOneField(InfoEntry, verbose_name='Статья', related_name='info_entry_statistics',
                                      on_delete=models.CASCADE, blank=True, null=True)
    news = models.OneToOneField(New, verbose_name='Новость', related_name='info_news_statistics',
                                      on_delete=models.CASCADE, blank=True, null=True)
    total_views = models.PositiveIntegerField('Всего просмотров', default=0)

    def __str__(self):
        if self.info_entry:
            return f'Статистика статьи "{self.info_entry.name}"'
        else:
            return f'Статистика новости "{self.news.title}"'


class InfoEntryStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика статьи за месяц'
        verbose_name_plural = 'Статистика статьи за месяц'

    fk = models.ForeignKey(InfoEntryStatistics, verbose_name='Статистика статьи',
                           related_name='info_entry_statistics_month',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.name


class InfoEntryFileStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла статьи'
        verbose_name_plural = 'Статистика скачиваний файлов статей'

    info_entry = models.OneToOneField(InfoEntry, verbose_name='Статья', related_name='info_entry_file_statistics',
                                      on_delete=models.CASCADE, blank=True, null=True)
    news = models.OneToOneField(New, verbose_name='Новость', related_name='info_news_file_statistics',
                                on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.info_entry:
            return f'Статистика статьи "{self.info_entry.name}"'
        else:
            return f'Статистика новости "{self.news.title}"'


class InfoEntryFileStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачивания файла статьи за месяц'
        verbose_name_plural = 'Статистика скачивания файла статьи за месяц'

    fk = models.ForeignKey(InfoEntryFileStatistics, verbose_name='Статистика статьи',
                           related_name='info_entry_file_statistics_month',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество скачиваний файла (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество скачиваний файла (kg)', default=0)

    def __str__(self):
        return self.name


class InfoEntryListenStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи'
        verbose_name_plural = 'Статистика прослушиваний статей'

    info_entry = models.OneToOneField(InfoEntry, verbose_name='Статья', related_name='info_entry_listen_statistics',
                                      on_delete=models.CASCADE, blank=True, null=True)
    news = models.OneToOneField(New, verbose_name='Новость', related_name='info_news_listen_statistics',
                                on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.info_entry:
            return f'Статистика статьи "{self.info_entry.name}"'
        else:
            return f'Статистика новости "{self.news.title}"'

@receiver(post_save, sender=InfoEntry)
def create_statistics(sender, instance, created, **kwargs):
    if created:
        InfoEntryStatistics.objects.create(info_entry=instance)
        InfoEntryFileStatistics.objects.create(info_entry=instance)
        InfoEntryListenStatistics.objects.create(info_entry=instance)


@receiver(post_save, sender=New)
def create_news_statistics(sender, instance, created, **kwargs):
    if created:
        InfoEntryStatistics.objects.create(news=instance)
        InfoEntryFileStatistics.objects.create(news=instance)
        InfoEntryListenStatistics.objects.create(news=instance)


class InfoEntryListenStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи за месяц'
        verbose_name_plural = 'Статистика прослушиваний статьи за месяц'

    fk = models.ForeignKey(InfoEntryListenStatistics, verbose_name='Статистика статьи',
                           related_name='info_entry_listen_statistics_month',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество прослушиваний (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество прослушиваний (kg)', default=0)

    def __str__(self):
        return self.name
