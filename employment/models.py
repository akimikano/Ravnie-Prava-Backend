from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.extra import ContentTypeRestrictedFileField
from main.models import Section


TYPE_CHOICES = (
    ('site', 'Сайты'),
    ('info', 'Полезная информация'),
    ('audio', 'Статьи с аудио'),
    ('course', 'Курсы')
)

SUB_TYPE_CHOICES = (
    ('resume_application', 'Резюме/заявление'),
    ('audio', 'Аудиозапись'),
    ('course', 'Курс'),
    ('different', 'Другая информация')
)


class EmpHead(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, related_name='empheads_set',
                                verbose_name='Раздел')
    name = models.CharField('Название', max_length=250, default='')
    type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES, default='site')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.name


class Site(models.Model):
    head = models.ForeignKey('EmpHead', on_delete=models.CASCADE, related_name='sites_set', verbose_name='Глава')
    link = models.URLField('Ссылка', max_length=128, unique=True, blank=True)

    class Meta:
        verbose_name = 'Сайт для поиска работы'
        verbose_name_plural = 'Сайты для поиска работы'

    def __str__(self):
        return "%s" % self.link


class EmpSubhead(models.Model):
    name = models.CharField('Название', max_length=250, default='')
    head = models.ForeignKey('EmpHead', on_delete=models.CASCADE, related_name='subheads_set', verbose_name='Глава')
    type = models.CharField('Тип', max_length=20, choices=SUB_TYPE_CHOICES, default='resume_application')

    class Meta:
        verbose_name = 'Подглава'
        verbose_name_plural = 'Подглавы'

    def __str__(self):
        return self.name


class EmpEntryPhoto(models.Model):
    subhead = models.ForeignKey('EmpSubhead', on_delete=models.CASCADE, null=True, related_name='empentries_set',
                                verbose_name='Подглава')
    name = models.CharField('Название', max_length=250, default='')
    photo = models.FileField('Файл', blank=True, upload_to='employment/photos')
    audio_file = models.FileField(upload_to='employment/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='employment/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='employment/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')
    step = models.CharField('Шаг', max_length=100, default='')

    class Meta:
        verbose_name = 'Резюме/заявление'
        verbose_name_plural = 'Резюме/заявление'

    def __str__(self):
        return self.name


class EmpEntryAudio(models.Model):
    subhead = models.ForeignKey('EmpSubhead', on_delete=models.CASCADE, null=True, related_name='empentries_audio_set',
                                verbose_name='Подглава')
    name = models.CharField('Название', max_length=250, default='')
    file = ContentTypeRestrictedFileField(upload_to='employment/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    file_kg = ContentTypeRestrictedFileField(upload_to='employment/documents', blank=True, null=True,
                                          content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл (кырг.)',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='employment/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_file_kg = models.FileField(upload_to='employment/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио (кырг.)')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_duration_kg = models.PositiveIntegerField("Длительность аудио в секундах (кырг.)", blank=True, null=True)
    audio_image = models.FileField(upload_to='employment/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')

    class Meta:
        verbose_name = 'Статья с аудио'
        verbose_name_plural = 'Статьи с аудио'

    def __str__(self):
        return self.name


class Other(models.Model):
    head = models.ForeignKey('EmpHead', on_delete=models.CASCADE, null=True, related_name='others_set',
                                verbose_name='Глава')
    title = models.CharField('Заголовок', max_length=250, default='')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Др. информация'
        verbose_name_plural = 'Др. информация'

    def __str__(self):
        return self.title


class Course(models.Model):
    subhead = models.ForeignKey('EmpSubhead', on_delete=models.CASCADE, null=True,
                                related_name='courses_set', verbose_name='Подглава')
    category = models.CharField('Категория', max_length=250, default='')
    description = models.TextField('Описание', default='')
    name = models.CharField('Курс', max_length=250, default='')
    company = models.CharField('Название организации/компании', max_length=250, default='')
    phone = models.CharField('Телефон', max_length=13, default='')
    email = models.EmailField('Почта', default='')
    address = models.CharField('Адрес', max_length=250, default='')
    file = ContentTypeRestrictedFileField(upload_to='employment/documents', blank=True,
                                          null=True, content_types=['application/pdf', ],
                                          max_upload_size=5242880, verbose_name='Файл',
                                          help_text='Допустимый формат - .pdf')
    audio_file = models.FileField(upload_to='employment/audio', null=True, blank=True,
                                  help_text="Допустимые форматы - .mp3, .wav, .ogg",
                                  verbose_name='Аудио')
    audio_duration = models.PositiveIntegerField("Длительность аудио в секундах", blank=True, null=True)
    audio_image = models.FileField(upload_to='employment/images', null=True, blank=True,
                                   verbose_name='Фото для аудио')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class EmpEntryAudioStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотра статей'
        verbose_name_plural = 'Статистика просмотров статей'

    emp_entry = models.OneToOneField(EmpEntryAudio, verbose_name='Статья', related_name='emp_entry_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    course = models.OneToOneField(Course, verbose_name='Курс', related_name='course_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)
    resume = models.OneToOneField(EmpEntryPhoto, verbose_name='Резюме', related_name='resume_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)
    total_views = models.PositiveIntegerField('Всего просмотров', default=0)

    def __str__(self):
        if self.emp_entry:
            return f'Статистика "{self.emp_entry.name}"'
        elif self.course:
            return f'Статистика "{self.course.name}"'
        else:
            return f'Статистика "{self.resume.name}"'


class EmpEntryAudioStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика просмотра статьи за месяц'
        verbose_name_plural = 'Статистика просмотра статьи за месяц'

    fk = models.ForeignKey(EmpEntryAudioStatistics, verbose_name='',
                           related_name='emp_entry_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.name


class EmpEntryAudioFileStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний файла статьи'
        verbose_name_plural = 'Статистика скачиваний файлов статей'

    emp_entry = models.OneToOneField(EmpEntryAudio, verbose_name='Статья', related_name='emp_entry_file_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    course = models.OneToOneField(Course, verbose_name='Курс', related_name='course_file_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)
    resume = models.OneToOneField(EmpEntryPhoto, verbose_name='Резюме', related_name='resume_file_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.emp_entry:
            return f'Статистика "{self.emp_entry.name}"'
        elif self.course:
            return f'Статистика "{self.course.name}"'
        else:
            return f'Статистика "{self.resume.name}"'


class EmpEntryAudioFileStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика скачивания файла статьи за месяц'
        verbose_name_plural = 'Статистика скачивания файла статьи за месяц'

    fk = models.ForeignKey(EmpEntryAudioFileStatistics, verbose_name='',
                           related_name='emp_entry_file_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество скачиваний файла (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество скачиваний файла (kg)', default=0)

    def __str__(self):
        return self.name


class EmpEntryAudioListenStatistics(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи'
        verbose_name_plural = 'Статистика прослушиваний статей'

    emp_entry = models.OneToOneField(EmpEntryAudio, verbose_name='Статья', related_name='emp_entry_listen_statistics',
                                     on_delete=models.CASCADE, blank=True, null=True)
    course = models.OneToOneField(Course, verbose_name='Курс', related_name='course_listen_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)
    resume = models.OneToOneField(EmpEntryPhoto, verbose_name='Резюме', related_name='resume_listen_statistics',
                                  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.emp_entry:
            return f'Статистика "{self.emp_entry.name}"'
        elif self.course:
            return f'Статистика "{self.course.name}"'
        else:
            return f'Статистика "{self.resume.name}"'


@receiver(post_save, sender=EmpEntryAudio)
def create_statistics(sender, instance, created, **kwargs):
    if created:
        EmpEntryAudioStatistics.objects.create(emp_entry=instance)
        EmpEntryAudioFileStatistics.objects.create(emp_entry=instance)
        EmpEntryAudioListenStatistics.objects.create(emp_entry=instance)


@receiver(post_save, sender=EmpEntryPhoto)
def create_resume_statistics(sender, instance, created, **kwargs):
    if created:
        EmpEntryAudioStatistics.objects.create(resume=instance)
        EmpEntryAudioFileStatistics.objects.create(resume=instance)
        EmpEntryAudioListenStatistics.objects.create(resume=instance)


@receiver(post_save, sender=Course)
def create_course_statistics(sender, instance, created, **kwargs):
    if created:
        EmpEntryAudioStatistics.objects.create(course=instance)
        EmpEntryAudioFileStatistics.objects.create(course=instance)
        EmpEntryAudioListenStatistics.objects.create(course=instance)


class EmpEntryAudioListenStatisticsMonth(models.Model):

    class Meta:
        verbose_name = 'Статистика прослушиваний статьи за месяц'
        verbose_name_plural = 'Статистика прослушиваний статьи за месяц'

    fk = models.ForeignKey(EmpEntryAudioListenStatistics, verbose_name='',
                           related_name='emp_entry_listen_statistics_months',
                           on_delete=models.CASCADE)
    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    count = models.PositiveIntegerField('Количество прослушиваний (ru)', default=0)
    count_kg = models.PositiveIntegerField('Количество прослушиваний (kg)', default=0)

    def __str__(self):
        return self.name