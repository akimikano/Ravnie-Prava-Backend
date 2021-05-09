from rest_framework import serializers
from rest_framework.reverse import reverse

from base.models import Head, Entry, EntryStatistics


class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = ('id', 'name', 'description')


class EntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'name', 'audio_file', 'audio_image')


class EntryDetailSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    file_kg = serializers.SerializerMethodField()
    audio_file = serializers.SerializerMethodField()
    audio_file_kg = serializers.SerializerMethodField()
    download_link = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, default='baza')

    class Meta:
        model = Entry
        fields = ('id', 'name', 'file', 'file_kg', 'audio_file',
                  'audio_file_kg', 'audio_duration', 'audio_duration_kg',
                  'audio_image', 'download_link', 'download_link_kg', 'views', 'type')

    def get_file(self, obj):
        request = self.context.get('request')
        try:
            file = obj.file.url
        except:
            return None
        return request.build_absolute_uri(file)

    def get_file_kg(self, obj):
        request = self.context.get('request')
        try:
            file = obj.file_kg.url
        except:
            return None
        return request.build_absolute_uri(file)

    def get_audio_file(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file.url
        except:
            return None
        return request.build_absolute_uri(audio_file)

    def get_audio_file_kg(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file_kg.url
        except:
            return None
        return request.build_absolute_uri(audio_file)

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('base_entry_download', args=(obj.pk, )))

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('base_entry_download_kg', args=(obj.pk, )))

    def get_views(self, obj):
        try:
            statistics = EntryStatistics.objects.get(entry=obj)
        except:
            statistics = EntryStatistics.objects.create(entry=obj)
        return statistics.total_views
