from django.urls import path
from main.views import SectionAPIView


urlpatterns = [
    path('', SectionAPIView.as_view(), name='section'),
]