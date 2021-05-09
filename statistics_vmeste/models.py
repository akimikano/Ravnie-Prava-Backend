from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from info.models import InfoEntry


class AppDownloadStatisticsAndroid(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний приложения Android'
        verbose_name_plural = 'Статистика скачиваний приложения Android'

    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    total_count = models.PositiveIntegerField('Всего скачиваний за этот месяц', default=0)

    def __str__(self):
        return self.name


class AppDownloadStatisticsIOS(models.Model):

    class Meta:
        verbose_name = 'Статистика скачиваний приложения IOS'
        verbose_name_plural = 'Статистика скачиваний приложения IOS'

    name = models.CharField('Статистика', max_length=255, blank=True, null=True)
    date = models.DateField('Дата')
    total_count = models.PositiveIntegerField('Всего скачиваний за этот месяц', default=0)

    def __str__(self):
        return self.name


class AppDownloadsAndroid(models.Model):

    class Meta:
        verbose_name = 'Скачивание'
        verbose_name_plural = 'Скачивания'

    fk = models.ForeignKey(AppDownloadStatisticsAndroid, verbose_name='Статистика месяца Android',
                           related_name='android_downloads', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return f'№{self.id}'


class AppDownloadsIOS(models.Model):

    class Meta:
        verbose_name = 'Скачивание'
        verbose_name_plural = 'Скачивания'

    fk = models.ForeignKey(AppDownloadStatisticsIOS, verbose_name='Статистика месяца IOS',
                           related_name='ios_downloads', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'№{self.id}'
















