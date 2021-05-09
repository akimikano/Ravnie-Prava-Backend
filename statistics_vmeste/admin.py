from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.http import HttpResponseRedirect
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter

from statistics_vmeste.models import AppDownloadStatisticsAndroid, AppDownloadsAndroid, AppDownloadsIOS, \
    AppDownloadStatisticsIOS


class CustomAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def changelist_view(self, request, extra_context=None):
        total_downloads = self.get_total_downloads(request)
        extra_context = extra_context or {}
        extra_context['count'] = f'Всего скачиваний - {total_downloads}'
        return super(CustomAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_total_downloads(self, request):
        qs = self.get_changelist_instance(request).get_queryset(request)
        total_downloads = sum([i.total_count for i in qs])
        return total_downloads


class AppDownloadAndroidInline(admin.StackedInline):
    model = AppDownloadsAndroid
    readonly_fields = ('date',)
    ordering = ('-date',)
    extra = 0


class AppStatisticsAndroidAdmin(CustomAdmin):
    inlines = [AppDownloadAndroidInline]
    list_filter = (
        ('date', DateRangeFilter),
    )
    list_display = ('name', 'total_count',)
    fields = ('name', 'total_count')
    readonly_fields = ('name', 'total_count')

class AppDownloadIOSInline(admin.StackedInline):
    model = AppDownloadsIOS
    readonly_fields = ('date',)
    ordering = ('-date',)
    extra = 0


class AppStatisticsIOSAdmin(CustomAdmin):
    inlines = [AppDownloadIOSInline]
    list_filter = (
        ('date', DateRangeFilter),
    )
    list_display = ('name', 'total_count',)
    fields = ('name', 'total_count')
    readonly_fields = ('name', 'total_count')


admin.site.register(AppDownloadStatisticsAndroid, AppStatisticsAndroidAdmin)
admin.site.register(AppDownloadStatisticsIOS, AppStatisticsIOSAdmin)


class ViewsCounterInline(admin.TabularInline):
    exclude = ('date',)
    readonly_fields = ('name', 'count',)
    extra = 0
    ordering = ('-date',)
    date_start = None
    date_end = None

    def get_queryset(self, request, *obj):
        date_start = self.date_start
        date_end = self.date_end
        queryset = super().get_queryset(request)
        if date_start:
            date_start = date_start.split('/')
            date_start = f'{date_start[2]}-{date_start[0]}-{date_start[1]}'
            queryset = queryset.filter(date__gte=date_start)
        if date_end:
            date_end = date_end.split('/')
            date_end = f'{date_end[2]}-{date_end[0]}-{date_end[1]}'
            queryset = queryset.filter(date__lte=date_end)
        if obj:
            queryset = queryset.filter(fk=obj[0])
        return queryset

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj):
        return False


class ViewsCounterAdmin(admin.ModelAdmin):
    date_start = None
    date_end = None
    views_count = 0

    def get_views_count(self, obj):
        return self.views_count

    get_views_count.short_description = 'Всего просмотров'

    def get_inline_instances(self, request, obj=None):
        res_inlines = super().get_inline_instances(request, obj=None)
        for inline in res_inlines:
            if self.date_start:
                inline.date_start = self.date_start
                self.date_start = None
            if self.date_end:
                inline.date_end = self.date_end
                self.date_end = None
        inline_queryset = res_inlines[0].get_queryset(request, obj)
        views_count = sum([i['count'] for i in list(inline_queryset.values('count'))])
        self.views_count = views_count
        return res_inlines

    def response_change(self, request, obj):
        if "use_filter" in request.POST:
            date_start = request.POST.get('date_start', None)
            date_end = request.POST.get('date_end', None)
            self.date_start = date_start if date_start else None
            self.date_end = date_end if date_end else None
            return HttpResponseRedirect(".")
        elif "get_all" in request.POST:
            self.date_start = None
            self.date_end = None
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False


class FileStatisticsInline(admin.TabularInline):
    exclude = ('date',)
    readonly_fields = ('name', 'count', 'count_kg')
    extra = 0
    ordering = ('-date',)
    date_start = None
    date_end = None

    def get_queryset(self, request):
        date_start = self.date_start
        date_end = self.date_end
        queryset = super().get_queryset(request)
        if date_start:
            date_start = date_start.split('/')
            date_start = f'{date_start[2]}-{date_start[0]}-{date_start[1]}'
            queryset = queryset.filter(date__gte=date_start)
        if date_end:
            date_end = date_end.split('/')
            date_end = f'{date_end[2]}-{date_end[0]}-{date_end[1]}'
            queryset = queryset.filter(date__lte=date_end)

        return queryset

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj):
        return False


class FileStatisticsAdmin(admin.ModelAdmin):
    date_start = None
    date_end = None
    downloads = 0
    downloads_kg = 0

    def get_downloads(self, obj):
        return self.downloads

    def get_downloads_kg(self, obj):
        return self.downloads_kg

    get_downloads.short_description = 'Всего скачиваний (ru)'
    get_downloads_kg.short_description = 'Всего скачиваний (kg)'

    def get_inline_instances(self, request, obj=None):
        res_inlines = []
        for inline in self.inlines:
            inline_instance = inline(self.model, self.admin_site)
            if self.date_start:
                inline_instance.date_start = self.date_start
            if self.date_end:
                inline_instance.date_end = self.date_end
            res_inlines.append(inline_instance)

        inline_queryset = res_inlines[0].get_queryset(request)
        inline_queryset = inline_queryset.filter(fk=obj)
        self.downloads = sum([i['count'] for i in list(inline_queryset.values('count'))])
        self.downloads_kg = sum([i['count_kg'] for i in list(inline_queryset.values('count_kg'))])

        return res_inlines

    def response_change(self, request, obj):
        if "use_filter" in request.POST:
            date_start = request.POST.get('date_start', None)
            date_end = request.POST.get('date_end', None)
            self.date_start = date_start if date_start else None
            self.date_end = date_end if date_end else None
            return HttpResponseRedirect(".")
        elif "get_all" in request.POST:
            self.date_start = None
            self.date_end = None
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False


class ListenedInline(admin.TabularInline):
    exclude = ('date',)
    readonly_fields = ('name', 'count', 'count_kg')
    extra = 0
    ordering = ('-date',)
    date_start = None
    date_end = None

    def get_queryset(self, request):
        date_start = self.date_start
        date_end = self.date_end
        queryset = super().get_queryset(request)
        if date_start:
            date_start = date_start.split('/')
            date_start = f'{date_start[2]}-{date_start[0]}-{date_start[1]}'
            queryset = queryset.filter(date__gte=date_start)
        if date_end:
            date_end = date_end.split('/')
            date_end = f'{date_end[2]}-{date_end[0]}-{date_end[1]}'
            queryset = queryset.filter(date__lte=date_end)

        return queryset

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj):
        return False


class ListenedAdmin(admin.ModelAdmin):
    date_start = None
    date_end = None
    listens = 0
    listens_kg = 0

    def get_listens(self, obj):
        return self.listens

    def get_listens_kg(self, obj):
        return self.listens_kg

    get_listens.short_description = 'Всего прослушиваний (ru)'
    get_listens_kg.short_description = 'Всего прослушиваний (kg)'

    def get_inline_instances(self, request, obj=None):
        res_inlines = []
        for inline in self.inlines:
            inline_instance = inline(self.model, self.admin_site)
            if self.date_start:
                inline_instance.date_start = self.date_start
            if self.date_end:
                inline_instance.date_end = self.date_end
            res_inlines.append(inline_instance)

        inline_queryset = res_inlines[0].get_queryset(request)
        inline_queryset = inline_queryset.filter(fk=obj)
        self.listens = sum([i['count'] for i in list(inline_queryset.values('count'))])
        self.listens_kg = sum([i['count_kg'] for i in list(inline_queryset.values('count_kg'))])
        print(self.listens)

        return res_inlines

    def response_change(self, request, obj):
        if "use_filter" in request.POST:
            date_start = request.POST.get('date_start', None)
            date_end = request.POST.get('date_end', None)
            self.date_start = date_start if date_start else None
            self.date_end = date_end if date_end else None
            return HttpResponseRedirect(".")
        elif "get_all" in request.POST:
            self.date_start = None
            self.date_end = None
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False
