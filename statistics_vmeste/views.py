from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from statistics_vmeste.models import AppDownloadStatisticsAndroid, AppDownloadsAndroid, AppDownloadStatisticsIOS, \
    AppDownloadsIOS
from statistics_vmeste.utils import increment_mobile_statistics


class AddToAndroidStatistics(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        datetime = date.today()
        month = datetime.month
        year = datetime.year
        try:
            increment_mobile_statistics(AppDownloadStatisticsAndroid, AppDownloadsAndroid)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class AddToIOSStatistics(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        datetime = date.today()
        month = datetime.month
        year = datetime.year
        try:
            increment_mobile_statistics(AppDownloadStatisticsIOS, AppDownloadsIOS)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})




