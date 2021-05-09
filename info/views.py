from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from employment.utils import increment_views_count, increment_downloads_count, increment_downloads_count_kg
from info.models import InfoHead, New, InfoSubhead, InfoEntry, InfoEntryFileStatistics, InfoEntryFileStatisticsMonth, \
    InfoEntryListenStatistics, InfoEntryListenStatisticsMonth
from info.serializers import InfoHeadSerializer, NewsListSerializer, NewsDetailSerializer, InfoSubheadSerializer, \
    InfoEntryListSerializer, InfoEntryDetailSerializer
from .models import InfoEntryStatistics, InfoEntryStatisticsMonth


class InfoHeadAPIView(ListAPIView):
    """
    Главы раздела (список)

    1. Без id
    get - list

    """
    queryset = InfoHead.objects.all()
    serializer_class = InfoHeadSerializer


class NewsListAPIView(ListAPIView):
    """
    Материалы из СМИ (список)

    1. Без id
    get - list

    """
    queryset = New.objects.all()
    serializer_class = NewsDetailSerializer


class NewsDetailAPIView(RetrieveAPIView):
    """
    Материалы из СМИ (детально)

    1. С id
    get - retrieve

    """
    queryset = New.objects.all()
    serializer_class = NewsDetailSerializer


class InfoSubheadListAPIView(ListAPIView):
    """
    Подглавы главы (список)

    1. Без id
    get - list

    """
    queryset = InfoSubhead.objects.all()
    serializer_class = InfoSubheadSerializer


@permission_classes((permissions.AllowAny,))
class InfoEntryListAPIView(APIView):
    """
    Статьи подглавы (список)

    1. Без id
    get - list

    """
    def get(self, request, pk):
        queryset = InfoEntry.objects.filter(subhead=pk)
        serializer = InfoEntryDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InfoEntryDetailAPIView(RetrieveAPIView):
    """
    Статья подглавы (детально)

    1. С id
    get - retrieve

    """
    queryset = InfoEntry.objects.all()
    serializer_class = InfoEntryDetailSerializer


@permission_classes((permissions.AllowAny,))
class MediaDownloadListAPIView(APIView):
    """
    Скачать файл (материалы из СМИ)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = New.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


@permission_classes((permissions.AllowAny,))
class MediaKgDownloadListAPIView(APIView):
    """
    Скачать файл (материалы из СМИ)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = New.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


@permission_classes((permissions.AllowAny,))
class FileDownloadListAPIView(APIView):
    """
    Скачать файл (публикация)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = InfoEntry.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


@permission_classes((permissions.AllowAny,))
class FileKgDownloadListAPIView(APIView):
    """
    Скачать файл (публикация)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = InfoEntry.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


class InfoEntryListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryListenStatistics.objects.get(info_entry_id=kwargs['id'])
        except:
            statistics = InfoEntryListenStatistics.objects.create(info_entry_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, InfoEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class InfoEntryListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryListenStatistics.objects.get(info_entry_id=kwargs['id'])
        except:
            statistics = InfoEntryListenStatistics.objects.create(info_entry_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, InfoEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class InfoEntryCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryStatistics.objects.get(info_entry_id=kwargs['id'])
        except:
            statistics = InfoEntryStatistics.objects.create(info_entry_id=kwargs['id'])

        try:
            increment_views_count(statistics, InfoEntryStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class InfoEntryDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryFileStatistics.objects.get(info_entry_id=kwargs['id'])
        except:
            statistics = InfoEntryFileStatistics.objects.create(info_entry_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, InfoEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class InfoEntryDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryFileStatistics.objects.get(info_entry_id=kwargs['id'])
        except:
            statistics = InfoEntryFileStatistics.objects.create(info_entry_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, InfoEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class NewListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryListenStatistics.objects.get(news_id=kwargs['id'])
        except:
            statistics = InfoEntryListenStatistics.objects.create(news_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, InfoEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class NewListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryListenStatistics.objects.get(news_id=kwargs['id'])
        except:
            statistics = InfoEntryListenStatistics.objects.create(news_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, InfoEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class NewCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryStatistics.objects.get(news_id=kwargs['id'])
        except:
            statistics = InfoEntryStatistics.objects.create(news_id=kwargs['id'])

        try:
            increment_views_count(statistics, InfoEntryStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class NewDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryFileStatistics.objects.get(news_id=kwargs['id'])
        except:
            statistics = InfoEntryFileStatistics.objects.create(news_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, InfoEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class NewDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = InfoEntryFileStatistics.objects.get(news_id=kwargs['id'])
        except:
            statistics = InfoEntryFileStatistics.objects.create(news_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, InfoEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})
