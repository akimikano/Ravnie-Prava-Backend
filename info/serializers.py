from rest_framework import serializers
from rest_framework.reverse import reverse

from info.models import InfoHead, New, InfoSubhead, InfoEntry, InfoEntryStatistics


class InfoHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoHead
        fields = ('id', 'name', 'description', 'type')


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'date')


class NewsDetailSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = New
        fields = ('id', 'title', 'text', 'photo', 'date',
                  'audio_file', 'audio_file_kg', 'audio_duration',
                  'audio_duration_kg', 'audio_image',
                  'download_link', 'download_link_kg', 'type')

    def get_type(self, obj):
        return 'info/news'

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('info_media_download', args=(obj.pk, )))

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('info_media_download_kg', args=(obj.pk, )))


class InfoSubheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoSubhead
        fields = ('id', 'name')


class InfoEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoEntry
        fields = ('id', 'name', 'audio_file', 'audio_image')


class InfoEntryDetailSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, default='info')

    class Meta:
        model = InfoEntry
        fields = ('id', 'name', 'text', 'photo',
                  'date', 'file', 'file_kg', 'audio_file',
                  'audio_file_kg', 'audio_duration', 'audio_duration_kg',
                  'audio_image', 'download_link', 'download_link_kg', 'views', 'type')

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('info_entry_download', args=(obj.pk, )))

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('info_entry_download_kg', args=(obj.pk, )))

    def get_views(self, obj):
        try:
            statistics = InfoEntryStatistics.objects.get(info_entry=obj)
        except:
            statistics = InfoEntryStatistics.objects.create(info_entry=obj)
        return statistics.total_views
