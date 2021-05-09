import mutagen
from django.contrib import admin
from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from bookkeeping.forms import BookkeepingStatisticsForm, BookkeepingFileStatisticsForm, BookkeepingListenStatisticsForm
from bookkeeping.models import BookKeeping, BookkeepingStatisticsMonth, BookkeepingStatistics, \
    BookkeepingFileStatisticsMonth, BookkeepingFileStatistics, BookkeepingListenStatisticsMonth, \
    BookkeepingListenStatistics
from statistics_vmeste.admin import ViewsCounterInline, ViewsCounterAdmin, FileStatisticsInline, FileStatisticsAdmin, \
    ListenedInline, ListenedAdmin


@receiver(pre_save, sender=BookKeeping)
def some_pre_save_receiver(sender, instance, raw, using, update_fields, **kwargs):
    file_was_updated = False
    file_kg_was_updated = False
    if instance.audio_file:
        file_was_updated = True

    if update_fields and "audio_file" in update_fields:
        file_was_updated = True

    if instance.audio_file_kg:
        file_kg_was_updated = True

    if update_fields and "audio_file_kg" in update_fields:
        file_kg_was_updated = True

    if file_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.audio_file).info
        # set audio duration in seconds, so we can access it in database
        instance.audio_duration = int(audio_info.length)

    if file_kg_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.audio_file_kg).info
        # set audio duration in seconds, so we can access it in database
        instance.audio_duration_kg = int(audio_info.length)


class BookkeepingStatisticsMonthInline(ViewsCounterInline):
    model = BookkeepingStatisticsMonth


class BookkeepingStatisticsAdmin(ViewsCounterAdmin):
    form = BookkeepingStatisticsForm
    inlines = [BookkeepingStatisticsMonthInline]
    fields = ('bookkeeping', 'date_start', 'date_end', 'get_views_count')
    readonly_fields = ('bookkeeping', 'get_views_count')


class BookkeepingFileStatisticsMonthInline(FileStatisticsInline):
    model = BookkeepingFileStatisticsMonth


class BookkeepingFileStatisticsAdmin(FileStatisticsAdmin):
    form = BookkeepingFileStatisticsForm
    inlines = [BookkeepingFileStatisticsMonthInline]
    fields = ('bookkeeping', 'date_start', 'date_end', 'get_downloads', 'get_downloads_kg')
    readonly_fields = ('bookkeeping', 'get_downloads', 'get_downloads_kg')


class BookkeepingListenStatisticsMonthInline(ListenedInline):
    model = BookkeepingListenStatisticsMonth


class BookkeepingListenStatisticsAdmin(ListenedAdmin):
    form = BookkeepingListenStatisticsForm
    inlines = [BookkeepingListenStatisticsMonthInline]
    fields = ('bookkeeping', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
    readonly_fields = ('bookkeeping', 'get_listens', 'get_listens_kg')


admin.site.register(BookkeepingStatistics, BookkeepingStatisticsAdmin)
admin.site.register(BookkeepingFileStatistics, BookkeepingFileStatisticsAdmin)
admin.site.register(BookkeepingListenStatistics, BookkeepingListenStatisticsAdmin)
admin.site.register(BookKeeping)

