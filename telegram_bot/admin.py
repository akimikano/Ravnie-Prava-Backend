from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from telegram_bot.models import TelegramReceiver, FeedbackApplication


class TelegramAdmin(admin.ModelAdmin):
    readonly_fields = ('telegram_id',)


class FeedbackApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_filter = (
        ('date', DateRangeFilter),
    )


admin.site.register(TelegramReceiver, TelegramAdmin)
admin.site.register(FeedbackApplication, FeedbackApplicationAdmin)
