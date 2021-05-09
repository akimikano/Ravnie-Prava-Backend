from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.extra import ContentTypeRestrictedFileField
from main.models import Section


class BookKeeping(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE, related_name='bookkeepings_set',
                                verbose_name='Раздел')
    name = models.CharField('Название', max_length=250, default='')
    file = ContentTypeRestrictedFileField(upload_to='bookkeeping/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='bookkeeping/documents', blank=True, null=True,
                                             content_types=['application/pdf', ],
                                             max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                             help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='bookkeeping/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='bookkeeping/audio', null=True, blank=True,
                                     help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                     verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='bookkeeping/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')
    type = models.CharField('Тип', max_length=20, default="Аудиозапись")

    class Meta:
        verbose_name = 'Полезная бухгалтерия'
        verbose_name_plural = 'Полезная бухгалтерия'

    def __str__(self):
        return self.name


class BookkeepingStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотра полезной бухгалтерии'
        verbose_name_plural = 'Статистика просмотров полезной бухгалтерии'

    bookkeeping = models.OneToOneField(BookKeeping, verbose_name='Полезная бухгалтерия', related_name='bookkeeping_statistics',
                                       on_delete=models.CASCADE)
    total_views = models.PositiveIntegerField('Всего просмотров', default=0)

    def __str__(self):
        return f'Статистика просмотров "{self.bookkeeping.name}"'


class BookkeepingStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика полезной бухгалтерии за месяц'
        verbose_name_plural = 'Статистика полезной бухгалтерии за месяц'

    fk = models.ForeignKey(BookkeepingStatistics, verbose_name='Полезная бухгалтерия',
                           related_name='bookkeeping_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.name


class BookkeepingFileStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла полезной бухгалтерии'
        verbose_name_plural = 'Статистика скачиваний файлов полезной бухгалтерии'

    bookkeeping = models.OneToOneField(BookKeeping, verbose_name='Полезная бухгалтерия',
                                       related_name='bookkeeping_file_statistics',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f'Статистика скачиваний файла "{self.bookkeeping.name}"'


class BookkeepingFileStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла полезной бухгалтерии за месяц'
        verbose_name_plural = 'Статистика скачиваний файла полезной бухгалтерии за месяц'

    fk = models.ForeignKey(BookkeepingFileStatistics, verbose_name='Полезная бухгалтерия',
                           related_name='bookkeeping_file_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество скачиваний файла (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество скачиваний файла (kg)', default=0)

    def __str__(self):
        return self.name


class BookkeepingListenStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний полезной бухгалтерии'
        verbose_name_plural = 'Статистика прослушиваний полезной бухгалтерии'

    bookkeeping = models.OneToOneField(BookKeeping, verbose_name='Полезная бухгалтерия',
                                       related_name='bookkeeping_listen_statistics',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f'Статистика прослушиваний "{self.bookkeeping.name}"'


@receiver(post_save, sender=BookKeeping)
def create_statistics(sender, instance, created, **kwargs):
    if created:
        BookkeepingStatistics.objects.create(bookkeeping=instance)
        BookkeepingFileStatistics.objects.create(bookkeeping=instance)
        BookkeepingListenStatistics.objects.create(bookkeeping=instance)


class BookkeepingListenStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний полезной бухгалтерии за месяц'
        verbose_name_plural = 'Статистика прослушиваний полезной бухгалтерии за месяц'

    fk = models.ForeignKey(BookkeepingListenStatistics, verbose_name='Полезная бухгалтерия',
                           related_name='bookkeeping_listen_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество прослушиваний (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество прослушиваний (kg)', default=0)

    def __str__(self):
        return self.name