from rest_framework import serializers
from rest_framework.reverse import reverse

from employment.models import EmpHead, Site, EmpSubhead, EmpEntryPhoto, Other, Course, EmpEntryAudio, \
    EmpEntryAudioStatistics


class EmpHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpHead
        fields = ('id', 'name', 'type')


class SiteTypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Site
        fields = ('id', 'name', 'type')

    def get_name(self, obj):
        return obj.link

    def get_type(self, obj):
        return "site"
        
        
class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = ('id', 'link')


class EmpSubheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSubhead
        fields = ('id', 'name', 'type')


class EmpEntryPhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpEntryPhoto
        fields = ('id', 'name')


class EmpEntryPhotoDetailSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    audio_file = serializers.SerializerMethodField()
    audio_file_kg = serializers.SerializerMethodField()
    download_link = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EmpEntryPhoto
        fields = ('id', 'name', 'file', 'audio_file', 'audio_file_kg',
                  'audio_duration', 'audio_duration_kg', 'audio_image',
                  'download_link', 'step', 'type')

    def get_type(self, obj):
        return 'resume'

    def get_file(self, obj):
        request = self.context.get('request')
        try:
            file = obj.photo.url
        except:
            file = None
        return request.build_absolute_uri(file)

    def get_audio_file(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file.url
        except:
            audio_file = None
        return request.build_absolute_uri(audio_file)

    def get_audio_file_kg(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file_kg.url
        except:
            audio_file = None
        return request.build_absolute_uri(audio_file)

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('employment_photo_download', args=(obj.pk, )))


class EmpEntryAudioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpEntryAudio
        fields = ('id', 'name')


class EmpEntryAudioDetailSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    audio_file = serializers.SerializerMethodField()
    download_link = serializers.SerializerMethodField()
    file_kg = serializers.SerializerMethodField()
    audio_file_kg = serializers.SerializerMethodField()
    download_link_kg = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(read_only=True, default='trud')

    class Meta:
        model = EmpEntryAudio
        fields = ('id', 'name', 'file', 'file_kg', 'audio_file', 'audio_file_kg',
                  'audio_duration', 'audio_duration_kg', 'audio_image',
                  'download_link', 'download_link_kg', 'views', 'type')

    def get_file(self, obj):
        request = self.context.get('request')
        try:
            file = obj.file.url
        except:
            file = None
        return request.build_absolute_uri(file)

    def get_audio_file(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file.url
        except:
            audio_file = None
        return request.build_absolute_uri(audio_file)

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('employment_audio_download', args=(obj.pk, )))

    def get_file_kg(self, obj):
        request = self.context.get('request')
        try:
            file = obj.file_kg.url
        except:
            file = None
        return request.build_absolute_uri(file)

    def get_audio_file_kg(self, obj):
        request = self.context.get('request')
        try:
            audio_file = obj.audio_file_kg.url
        except:
            audio_file = None
        return request.build_absolute_uri(audio_file)

    def get_download_link_kg(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('employment_audio_download_kg', args=(obj.pk, )))

    def get_views(self, obj):
        try:
            statistics = EmpEntryAudioStatistics.objects.get(emp_entry=obj)
        except:
            statistics = EmpEntryAudioStatistics.objects.create(emp_entry=obj)
        return statistics.total_views


class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = ('id', 'title', 'text')


class OtherTypeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Other
        fields = ('id', 'name', 'type')

    def get_type(self, obj):
        return "other"

    def get_name(self, obj):
        return obj.title


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'category', 'name', )


class CourseDetailSerializer(serializers.ModelSerializer):
    download_link = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'category', 'description', 'name', 'company', 'phone',
                  'email', 'address', 'audio_file', 'audio_duration',
                  'audio_image', 'download_link', 'type')

    def get_type(self, obj):
        return 'course'

    def get_download_link(self, obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(reverse('employment_course_download', args=(obj.pk, )))
