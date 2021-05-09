from rest_framework import serializers
from rest_framework.reverse import reverse

from bookkeeping.models import BookKeeping, BookkeepingStatistics


class BookKeepingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookKeeping
        fields = ('id', 'name', 'audio_file', 'audio_image')


class BookKeepingDetailSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField(read_only=True)
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BookKeeping
        fields = ('id', 'name', 'file', 'file_kg', 'audio_file', 'audio_file_kg',
                  'audio_duration', 'audio_duration_kg', 'audio_image',
                  'download_link', 'download_link_kg', 'views', 'type')

    def get_type(self, obj):
        return 'buhgalteriya'

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('bookkeeping_download', args=(obj.pk,)))

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('bookkeeping_download_kg', args=(obj.pk,)))

    def get_views(self, obj):
        try:
            statistics = BookkeepingStatistics.objects.get(bookkeeping=obj)
        except:
            statistics = BookkeepingStatistics.objects.create(bookkeeping=obj)
        return statistics.total_views
