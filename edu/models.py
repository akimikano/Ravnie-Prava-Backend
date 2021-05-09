from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.extra import ContentTypeRestrictedFileField
from main.models import Section


TYPE_CHOICES = (
    ('audio', 'Аудиозапись'),
    ('lawyer', 'Юрист'),
    ('organisation', 'Организация')
)


class EduHead(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='eduheads_set', verbose_name='Раздел')
    name = models.CharField('Название', max_length=250, default='')
    description = models.CharField('Краткая информация', max_length=250, default='')
    type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES, default='audio')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.name


class EduEntry(models.Model):
    head = models.ForeignKey('EduHead', on_delete=models.CASCADE, related_name='articles_set', verbose_name='Глава')
    name = models.CharField('Статья', max_length=250, default='')
    file = ContentTypeRestrictedFileField(upload_to='edu/documents', blank=True, null=True, content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='edu/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='edu/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='edu/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='edu/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name


class Lawyer(models.Model):
    head = models.ForeignKey('EduHead', on_delete=models.CASCADE, related_name='lawyers_set', verbose_name='Глава')
    name = models.CharField('ФИО', max_length=250, default='')
    phone = models.CharField('Телефон', max_length=13, default='')
    address = models.CharField('Адрес', max_length=250, default='')

    class Meta:
        verbose_name = 'Юрист'
        verbose_name_plural = 'Юристы'

    def __str__(self):
        return self.name


class Entity(models.Model):
    head = models.ForeignKey('EduHead', on_delete=models.CASCADE, related_name='entities_set', verbose_name='Глава')
    name = models.CharField('Название', max_length=250, default='')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('Название', max_length=250, default='')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Dept(models.Model):
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE, related_name='depts_set', verbose_name='Организация')
    name = models.CharField('Название', max_length=250, default='')
    phone = models.CharField('Телефон', max_length=13, default='')
    email = models.EmailField('Почта', default='')
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='depts_set', verbose_name='Город')
    address = models.CharField('Адрес', max_length=250, default='')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class EduEntryStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотра статьи'
        verbose_name_plural = 'Статистика просмотров статей'

    edu_entry = models.OneToOneField(EduEntry, verbose_name='Статья', related_name='edu_entry_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    dept = models.OneToOneField(Dept, verbose_name='Отдел', related_name='dept_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    total_views = models.PositiveIntegerField('Всего просмотров', default=0)

    def __str__(self):
        if self.edu_entry:
            return f'Статистика "{self.edu_entry.name}"'
        else:
            return f'Статистика "{self.dept.name}"'


class EduEntryStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика статьи за месяц'
        verbose_name_plural = 'Статистика статьи за месяц'

    fk = models.ForeignKey(EduEntryStatistics, verbose_name='Статья',
                           related_name='edu_entry_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.name


class EduEntryFileStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика скачивания файлов статьи'
        verbose_name_plural = 'Статистика скачиваний файлов статей'

    edu_entry = models.OneToOneField(EduEntry, verbose_name='Статья', related_name='edu_entry_file_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    dept = models.OneToOneField(Dept, verbose_name='Отдел', related_name='dept_file_statistics',
                                on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Статистика "{self.edu_entry.name}"'


class EduEntryFileStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файлов статьи за месяц'
        verbose_name_plural = 'Статистика скачиваний файлов статьи за месяц'

    fk = models.ForeignKey(EduEntryFileStatistics, verbose_name='Статья',
                           related_name='edu_entry_file_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество скачиваний файла (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество скачиваний файла (kg)', default=0)

    def __str__(self):
        return self.name


class EduEntryListenStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи'
        verbose_name_plural = 'Статистика прослушиваний статей'

    edu_entry = models.OneToOneField(EduEntry, verbose_name='Статья', related_name='edu_entry_listen_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    dept = models.OneToOneField(Dept, verbose_name='Отдел', related_name='dept_listen_statistics',
                                on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Статистика "{self.edu_entry.name}"'


@receiver(post_save, sender=EduEntry)
def create_statistics(sender, instance, created, **kwargs):
    if created:
        EduEntryStatistics.objects.create(edu_entry=instance)
        EduEntryFileStatistics.objects.create(edu_entry=instance)
        EduEntryListenStatistics.objects.create(edu_entry=instance)


@receiver(post_save, sender=Dept)
def create_dept_statistics(sender, instance, created, **kwargs):
    if created:
        EduEntryStatistics.objects.create(dept=instance)
        EduEntryFileStatistics.objects.create(dept=instance)
        EduEntryListenStatistics.objects.create(dept=instance)


class EduEntryListenStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи за месяц'
        verbose_name_plural = 'Статистика прослушиваний статей за месяц'

    fk = models.ForeignKey(EduEntryListenStatistics, verbose_name='Статья',
                           related_name='edu_entry_listen_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество просмотров файла (kg)', default=0)

    def __str__(self):
        return self.name
