from rest_framework import serializers

from telegram_bot.models import FeedbackApplication


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackApplication
        fields = ('name', 'surname', 'patronymic', 'number')
