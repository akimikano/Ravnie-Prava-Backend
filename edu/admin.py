import mutagen
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from edu.forms import EduEntryStatisticsForm, EduEntryFileStatisticsForm, EduEntryListenStatisticsForm
from edu.models import EduHead, EduEntry, Lawyer, Entity, City, Dept, EduEntryStatisticsMonth, EduEntryStatistics, \
    EduEntryFileStatisticsMonth, EduEntryFileStatistics, EduEntryListenStatisticsMonth, EduEntryListenStatistics
from statistics_vmeste.admin import ViewsCounterInline, ViewsCounterAdmin, FileStatisticsInline, FileStatisticsAdmin, \
    ListenedInline, ListenedAdmin


class EduEntryAdmin(admin.StackedInline):
    model = EduEntry
    extra = 0
    list_display = ('name', )


class LawyerAdmin(admin.StackedInline):
    model = Lawyer
    extra = 0


class EntityAdmin(admin.StackedInline):
    model = Entity
    extra = 0


class DeptAdmin(admin.ModelAdmin):
    model = Dept
    exclude = ('type', )


class EduHeadAdmin(admin.ModelAdmin):
    inlines = [
        EduEntryAdmin,
        LawyerAdmin,
        EntityAdmin,
    ]


@receiver(pre_save, sender=EduEntry)
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


class EduEntryStatisticsMonthInline(ViewsCounterInline):
    model = EduEntryStatisticsMonth


class EduEntryStatisticsAdmin(ViewsCounterAdmin):
    form = EduEntryStatisticsForm
    inlines = [EduEntryStatisticsMonthInline]
    fields = ('edu_entry', 'dept', 'date_start', 'date_end', 'get_views_count')
    readonly_fields = ('edu_entry', 'dept', 'get_views_count')


class EduEntryFileStatisticsMonthInline(FileStatisticsInline):
    model = EduEntryFileStatisticsMonth


class EduEntryFileStatisticsAdmin(FileStatisticsAdmin):
    form = EduEntryFileStatisticsForm
    inlines = [EduEntryFileStatisticsMonthInline]
    fields = ('edu_entry', 'dept', 'date_start', 'date_end', 'get_downloads', 'get_downloads_kg')
    readonly_fields = ('edu_entry', 'dept', 'get_downloads', 'get_downloads_kg')


class EduEntryListenStatisticsMonthInline(ListenedInline):
    model = EduEntryListenStatisticsMonth


class EduEntryListenStatisticsAdmin(ListenedAdmin):
    form = EduEntryListenStatisticsForm
    inlines = [EduEntryListenStatisticsMonthInline]
    fields = ('edu_entry', 'dept', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
    readonly_fields = ('edu_entry', 'dept', 'get_listens', 'get_listens_kg')


admin.site.register(EduEntryStatistics, EduEntryStatisticsAdmin)
admin.site.register(EduEntryFileStatistics, EduEntryFileStatisticsAdmin)
admin.site.register(EduEntryListenStatistics, EduEntryListenStatisticsAdmin)
admin.site.register(EduHead, EduHeadAdmin)
admin.site.register(City)
admin.site.register(Dept, DeptAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
