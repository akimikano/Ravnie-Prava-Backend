import mutagen
from django.contrib import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from info.forms import InfoEntryStatisticsForm, InfoEntryFileStatisticsForm, InfoEntryListenStatisticsForm
from info.models import InfoHead, New, InfoSubhead, InfoEntry, InfoEntryStatisticsMonth, InfoEntryStatistics, \
    InfoEntryFileStatisticsMonth, InfoEntryFileStatistics, InfoEntryListenStatisticsMonth, InfoEntryListenStatistics
from statistics_vmeste.admin import ViewsCounterInline, ViewsCounterAdmin, FileStatisticsInline, FileStatisticsAdmin, \
    ListenedInline, ListenedAdmin


class EntryInline(admin.StackedInline):
    model = InfoEntry
    extra = 0
    list_display = ('name', )


class NewsInline(admin.StackedInline):
    model = New
    extra = 0
    list_display = ('title', )


class SubheadInline(admin.StackedInline):
    model = InfoSubhead
    extra = 0
    readonly_fields = ["get_edit_link", ]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return mark_safe(u'<a href="{url}">{text}</a>'.format(
                url=url,
                text="Добавить статьи в данной подглаве"
            ))
        return "(Нажмите 'сохранить и продолжить редактирование', чтобы добавить статьи в данной подглаве)"
    get_edit_link.short_description = "Ссылка на редактирование"
    get_edit_link.allow_tags = True


@admin.register(InfoHead)
class HeadAdmin(admin.ModelAdmin):
    fields = ["name", 'type']
    inlines = [SubheadInline, NewsInline]


@admin.register(InfoSubhead)
class SubheadAdmin(admin.ModelAdmin):
    inlines = [EntryInline, ]


@receiver(pre_save, sender=New)
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


@receiver(pre_save, sender=InfoEntry)
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


class InfoEntryStatisticsMonthInline(ViewsCounterInline):
    model = InfoEntryStatisticsMonth


class InfoEntryStatisticsAdmin(ViewsCounterAdmin):
    form = InfoEntryStatisticsForm
    inlines = [InfoEntryStatisticsMonthInline]
    fields = ('info_entry', 'date_start', 'date_end', 'get_views_count')
    readonly_fields = ('info_entry', 'get_views_count')


class InfoEntryFileStatisticsMonthInline(FileStatisticsInline):
    model = InfoEntryFileStatisticsMonth


class InfoEntryFileStatisticsAdmin(FileStatisticsAdmin):
    form = InfoEntryFileStatisticsForm
    inlines = [InfoEntryFileStatisticsMonthInline]
    fields = ('info_entry', 'date_start', 'date_end', 'get_downloads', 'get_downloads_kg')
    readonly_fields = ('info_entry', 'get_downloads', 'get_downloads_kg')


class InfoEntryListenStatisticsMonthInline(ListenedInline):
    model = InfoEntryListenStatisticsMonth


class InfoEntryListenStatisticsAdmin(ListenedAdmin):
    form = InfoEntryListenStatisticsForm
    inlines = [InfoEntryListenStatisticsMonthInline]
    fields = ('info_entry', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
    readonly_fields = ('info_entry', 'get_listens', 'get_listens_kg')


admin.site.register(InfoEntryStatistics, InfoEntryStatisticsAdmin)
admin.site.register(InfoEntryFileStatistics, InfoEntryFileStatisticsAdmin)
admin.site.register(InfoEntryListenStatistics, InfoEntryListenStatisticsAdmin)
# admin.site.register(InfoHead)
# admin.site.register(New)
# admin.site.register(InfoSubhead)
# admin.site.register(InfoEntry, InfoEntryAdmin)
