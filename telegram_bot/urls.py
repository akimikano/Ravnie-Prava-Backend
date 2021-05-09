from django.urls import path

from telegram_bot.views import FeedbackView

urlpatterns = [
    path('send/', FeedbackView.as_view({'post': 'create'})),
]