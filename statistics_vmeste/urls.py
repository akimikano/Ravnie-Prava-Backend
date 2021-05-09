from django.urls import path

from statistics_vmeste.views import AddToAndroidStatistics, AddToIOSStatistics

urlpatterns = [
    path('android/', AddToAndroidStatistics.as_view()),
    path('ios/', AddToIOSStatistics.as_view()),
]