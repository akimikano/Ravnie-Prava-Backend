import mutagen
from django.contrib import admin
from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from statistics_vmeste.admin import ViewsCounterAdmin, ViewsCounterInline, FileStatisticsInline, FileStatisticsAdmin, \
    ListenedInline, ListenedAdmin
from .forms import EntryStatisticsForm, EntryFileStatisticsForm, EntryListenStatisticsForm
from .models import Head, Entry, EntryStatisticsMonth, EntryStatistics, EntryFileStatistics, EntryFileStatisticsMonth, \
    EntryListenStatisticsMonth, EntryListenStatistics


class EntryAdmin(admin.StackedInline):
    model = Entry
    extra = 1
    list_display = ('name', )
    readonly_fields = ('audio_duration', 'audio_duration_kg')


@receiver(pre_save, sender=Entry)
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


class HeadAdmin(admin.ModelAdmin):
    inlines = [
        EntryAdmin,
    ]


#class AudioWidget(forms.FileInput):
#   class Media:
#        css = {'all': ("https://gitcdn.github.io/bootstrap-toggle/2.2.2/css/bootstrap-toggle.min.css",)}
#
#    def render(self, name, value, attrs=None, renderer=None):
#        html = super(AudioWidget, self).render(name, value, attrs)
#        html = html + f"""
#        <div>
#            <audio controls>
#              <source src="{str(value.url)}" type="audio/ogg">
#              <source src="/{str(value.url)}" type="audio/mpeg">
#                Your browser does not support the audio element.
#            </audio>
#        </div>
#        """
#        return mark_safe(html)


#class AudioAdmin(admin.ModelAdmin):
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name == 'audio_file':
#            kwargs['widget'] = AudioWidget
#        return super(AudioAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class EntryStatisticsMonthInline(ViewsCounterInline):
    model = EntryStatisticsMonth


class EntryStatisticsAdmin(ViewsCounterAdmin):
    form = EntryStatisticsForm
    inlines = [EntryStatisticsMonthInline]
    fields = ('entry', 'date_start', 'date_end', 'get_views_count')
    readonly_fields = ('entry', 'get_views_count')


class EntryFileStatisticsMonthInline(FileStatisticsInline):
    model = EntryFileStatisticsMonth


class EntryFileStatisticsAdmin(FileStatisticsAdmin):
    form = EntryFileStatisticsForm
    inlines = [EntryFileStatisticsMonthInline]
    fields = ('entry', 'date_start', 'date_end', 'get_downloads', 'get_downloads_kg')
    readonly_fields = ('entry', 'get_downloads', 'get_downloads_kg')


class EntryListenStatisticsMonthInline(ListenedInline):
    model = EntryListenStatisticsMonth


class EntryListenStatisticsAdmin(ListenedAdmin):
    form = EntryListenStatisticsForm
    inlines = [EntryListenStatisticsMonthInline]
    fields = ('entry', 'date_start', 'date_end', 'get_listens', 'get_listens_kg')
    readonly_fields = ('entry', 'get_listens', 'get_listens_kg')


admin.site.register(Head, HeadAdmin)
admin.site.register(EntryStatistics, EntryStatisticsAdmin)
admin.site.register(EntryFileStatistics, EntryFileStatisticsAdmin)
admin.site.register(EntryListenStatistics, EntryListenStatisticsAdmin)
#admin.site.register(Entry, AudioAdmin)



