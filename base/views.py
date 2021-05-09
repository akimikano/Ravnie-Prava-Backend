from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Head, Entry, EntryStatisticsMonth, EntryStatistics, EntryFileStatistics, \
    EntryFileStatisticsMonth, EntryListenStatistics, EntryListenStatisticsMonth
from base.serializers import HeadSerializer, EntryDetailSerializer, EntryListSerializer
from rest_framework import generics, status, permissions
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from employment.utils import increment_downloads_count, increment_downloads_count_kg, increment_views_count


@permission_classes((permissions.AllowAny,))
class FileDownloadListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = Entry.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


@permission_classes((permissions.AllowAny,))
class FileKgDownloadListAPIView(APIView):
    """
    Скачать файл (кырг)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = Entry.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


class HeadAPIView(ListAPIView):
    """
    Главы раздела (список)

    1. Без id
    get - list

    """
    queryset = Head.objects.all()
    serializer_class = HeadSerializer


@permission_classes((permissions.AllowAny,))
class EntryListAPIView(APIView):
    """
    Статьи главы (список)

    1. Без ID
    get - list

    """

    def get(self, request, pk):
        queryset = Entry.objects.filter(head=pk)
        serializer = EntryDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EntryDetailAPIView(RetrieveAPIView):
    """
    Статья главы (детально)

    1. C ID
    get - retrieve

    """
    queryset = Entry.objects.all()
    serializer_class = EntryDetailSerializer


class EntryListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EntryListenStatistics.objects.get(entry_id=kwargs['id'])
        except:
            statistics = EntryListenStatistics.objects.create(entry_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, EntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EntryListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EntryListenStatistics.objects.get(entry_id=kwargs['id'])
        except:
            statistics = EntryListenStatistics.objects.create(entry_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, EntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EntryCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EntryStatistics.objects.get(entry_id=kwargs['id'])
        except:
            statistics = EntryStatistics.objects.create(entry_id=kwargs['id'])

        try:
            increment_views_count(statistics, EntryStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EntryFileDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EntryFileStatistics.objects.get(entry_id=kwargs['id'])
        except:
            statistics = EntryFileStatistics.objects.create(entry_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, EntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EntryFileDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EntryFileStatistics.objects.get(entry_id=kwargs['id'])
        except:
            statistics = EntryFileStatistics.objects.create(entry_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, EntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})







