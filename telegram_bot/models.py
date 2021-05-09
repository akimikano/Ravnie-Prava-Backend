from django.db import models


class TelegramReceiver(models.Model):
    class Meta:
        verbose_name_plural = 'Telegram получатели'
        verbose_name = 'Telegram получатель'

    telegram_login = models.CharField('Логин Telegram', help_text='С учетом регистра!', max_length=128, unique=True)
    telegram_id = models.IntegerField('Telegram ID', blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.telegram_login}'


class FeedbackApplication(models.Model):
    class Meta:
        verbose_name = 'Заявка на обратную связь'
        verbose_name_plural = 'Заявки на обратную связь'

    name = models.CharField('Имя', max_length=128)
    surname = models.CharField('Фамилия', max_length=128)
    patronymic = models.CharField('Отчество', max_length=128)
    number = models.CharField('Номер телефона', max_length=15)
    date = models.DateField('Дата поступления заявки', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} | {self.number}'
