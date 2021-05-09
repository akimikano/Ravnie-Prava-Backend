from rest_framework import serializers
from main.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'icon')


