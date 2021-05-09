from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from telegram_bot.models import FeedbackApplication
from telegram_bot.serializers import FeedbackSerializer
from telegram_bot.utils import send_msg


class FeedbackView(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = FeedbackApplication.objects.all()

    def perform_create(self, serializer):
        send_msg(serializer)
        serializer.save()
