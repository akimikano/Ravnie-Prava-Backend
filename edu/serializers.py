from rest_framework import serializers
from rest_framework.reverse import reverse

from edu.models import EduHead, EduEntry, Lawyer, Entity, Dept, City, EduEntryStatistics


class EduHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduHead
        fields = ('id', 'name', 'description', 'type')


class EduEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduEntry
        fields = ('id', 'name', 'audio_file', 'audio_image')


class EduEntryDetailSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    audio_file = serializers.SerializerMethodField()
    download_link = serializers.SerializerMethodField()
    file_kg = serializers.SerializerMethodField()
    audio_file_kg = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, default='likbez')

    class Meta:
        model = EduEntry
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
            audio = obj.audio_file.url
        except:
            return None
        return request.build_absolute_uri(audio)

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
        return request.build_absolute_uri(reverse('edu_entry_download', args=(obj.pk, )))

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('base_entry_download_kg', args=(obj.pk, )))

    def get_views(self, obj):
        try:
            statistics = EduEntryStatistics.objects.get(edu_entry=obj)
        except:
            statistics = EduEntryStatistics.objects.create(edu_entry=obj)
        return statistics.total_views


class LawyerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ('id', 'name', )


class LawyerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ('id', 'name', 'phone', 'address',)


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class DeptListSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Dept
        fields = ('id', 'name', 'city', )


class DeptDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Dept
        fields = ('id', 'name', 'phone', 'email', 'city', 'address', )