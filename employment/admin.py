import mutagen
from django.contrib import admin
from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import force_text

from employment.forms import EmpEntryAudioStatisticsForm, EmpEntryAudioFileStatisticsForm, \
    EmpEntryAudioListenStatisticsForm
from employment.models import EmpHead, Site, EmpSubhead, EmpEntryPhoto, EmpEntryAudio, Other, Course, \
    EmpEntryAudioStatisticsMonth, EmpEntryAudioStatistics, EmpEntryAudioFileStatisticsMonth, \
    EmpEntryAudioFileStatistics, EmpEntryAudioListenStatisticsMonth, EmpEntryAudioListenStatistics
from django.utils.safestring import mark_safe

from statistics_vmeste.admin import ViewsCounterInline, ViewsCounterAdmin, FileStatisticsInline, FileStatisticsAdmin, \
    ListenedInline, ListenedAdmin


class EmpEntryAudioAdmin(admin.ModelAdmin):
    list_display = ('name', )


class EmpEntryPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubheadInline(admin.StackedInline):
    model = EmpSubhead
    extra = 0
    readonly_fields = ["get_edit_link", ]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return mark_safe(u'<a href="{url}">{text}</a>'.format(
                url=url,
                text="Добавить статьи  или курсы в данной подглаве"
            ))
        return "(Нажмите 'сохранить и продолжить редактирование', чтобы добавить статьи в данной подглаве)"
    get_edit_link.short_description = "Ссылка на редактирование"
    get_edit_link.allow_tags = True


class SiteInline(admin.StackedInline):
    model = Site
    extra = 0


class EntryInline(admin.StackedInline):
    model = EmpEntryPhoto
    extra = 0


class AudioEntryInline(admin.StackedInline):
    model = EmpEntryAudio
    extra = 0


class CourseInline(admin.StackedInline):
    model = Course
    extra = 0


class OtherInline(admin.StackedInline):
    model = Other
    extra = 0


@admin.register(EmpHead)
class HeadAdmin(admin.ModelAdmin):
    fields = ["name", 'type']
    inlines = [SubheadInline, SiteInline, OtherInline]


@admin.register(EmpSubhead)
class SubheadAdmin(admin.ModelAdmin):
    inlines = [EntryInline, CourseInline, AudioEntryInline]


@receiver(pre_save, sender=EmpEntryAudio)
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


@receiver(pre_save, sender=EmpEntryPhoto)
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


@receiver(pre_save, sender=Course)
def some_pre_save_receiver(sender, instance, raw, using, update_fields, **kwargs):
    file_was_updated = False
    if instance.audio_file:
        file_was_updated = True

    if update_fields and "audio_file" in update_fields:
        file_was_updated = True

    if file_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.audio_file).info
        # set audio duration in seconds, so we can access it in database
        instance.audio_duration = int(audio_info.length)


class EmpEntryAudioStatisticsMonthInline(ViewsCounterInline):
    model = EmpEntryAudioStatisticsMonth


class EmpEntryAudioStatisticsAdmin(ViewsCounterAdmin):
    form = EmpEntryAudioStatisticsForm
    inlines = [EmpEntryAudioStatisticsMonthInline]
    fields = ('emp_entry', 'course', 'resume', 'date_start', 'date_end', 'get_views_count')
    readonly_fields = ('emp_entry', 'course', 'resume', 'get_views_count')


class EmpEntryAudioFileStatisticsMonthInline(FileStatisticsInline):
    model = EmpEntryAudioFileStatisticsMonth


class EmpEntryAudioFileStatisticsAdmin(FileStatisticsAdmin):
    form = EmpEntryAudioFileStatisticsForm
    inlines = [EmpEntryAudioFileStatisticsMonthInline]
    fields = ('emp_entry', 'course', 'resume', 'date_start', 'date_end', 'get_downloads', 'get_downloads_kg')
    readonly_fields = ('emp_entry', 'course', 'resume', 'get_downloads', 'get_downloads_kg')


class EmpEntryAudioListenStatisticsMonthInline(ListenedInline):
    model = EmpEntryAudioListenStatisticsMonth


class EmpEntryAudioListenStatisticsAdmin(ListenedAdmin):
    form = EmpEntryAudioListenStatisticsForm
    inlines = [EmpEntryAudioListenStatisticsMonthInline]
    fields = ('emp_entry', 'course', 'resume', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
    readonly_fields = ('emp_entry', 'course', 'resume', 'get_listens', 'get_listens_kg')

    def get_fields(self, request, obj=None):
        if obj.course:
            fields = ('course', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
            return fields
        if obj.resume:
            fields = ('resume', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
            return fields
        else:
            return self.fields



#admin.site.register(Site)
#admin.site.register(Other)
#admin.site.register(Course, CourseAdmin)
# admin.site.register(EmpEntryAudio, EmpEntryAudioAdmin)
admin.site.register(EmpEntryAudioStatistics, EmpEntryAudioStatisticsAdmin)
admin.site.register(EmpEntryAudioFileStatistics, EmpEntryAudioFileStatisticsAdmin)
admin.site.register(EmpEntryAudioListenStatistics, EmpEntryAudioListenStatisticsAdmin)
