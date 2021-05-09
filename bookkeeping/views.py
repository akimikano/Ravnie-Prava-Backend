from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from bookkeeping.models import BookKeeping, BookkeepingStatistics, BookkeepingStatisticsMonth, \
    BookkeepingFileStatistics, BookkeepingFileStatisticsMonth, BookkeepingListenStatistics, \
    BookkeepingListenStatisticsMonth
from bookkeeping.serializers import BookKeepingListSerializer, BookKeepingDetailSerializer
from employment.utils import increment_downloads_count_kg, increment_downloads_count, increment_views_count


class BookKeepingListAPIView(ListAPIView):
    """
    Статьи главы (список)

    1. Без ID
    get - list

    """
    queryset = BookKeeping.objects.all()
    serializer_class = BookKeepingDetailSerializer


class BookKeepingDetailAPIView(RetrieveAPIView):
    """
    Статья главы (детально)

    1. C ID
    get - retrieve

    """
    queryset = BookKeeping.objects.all()
    serializer_class = BookKeepingDetailSerializer


@permission_classes((permissions.AllowAny,))
class FileDownloadListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = BookKeeping.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


@permission_classes((permissions.AllowAny,))
class FileKgDownloadListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """

    def get(self, request, id, format=None):
        queryset = BookKeeping.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


class BookkeepingListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = BookkeepingListenStatistics.objects.get(bookkeeping_id=kwargs['id'])
        except:
            statistics = BookkeepingListenStatistics.objects.create(bookkeeping_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, BookkeepingListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class BookkeepingListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = BookkeepingListenStatistics.objects.get(bookkeeping_id=kwargs['id'])
        except:
            statistics = BookkeepingListenStatistics.objects.create(bookkeeping_id=kwargs['id'])

        try:
            increment_downloads_count_kg(statistics, BookkeepingListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class BookkeepingCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = BookkeepingStatistics.objects.get(bookkeeping_id=kwargs['id'])
        except:
            statistics = BookkeepingStatistics.objects.create(bookkeeping_id=kwargs['id'])

        try:
            increment_views_count(statistics, BookkeepingStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class BookkeepingDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = BookkeepingFileStatistics.objects.get(bookkeeping_id=kwargs['id'])
        except:
            statistics = BookkeepingFileStatistics.objects.create(bookkeeping_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, BookkeepingFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class BookkeepingDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = BookkeepingFileStatistics.objects.get(bookkeeping_id=kwargs['id'])
        except:
            statistics = BookkeepingFileStatistics.objects.create(bookkeeping_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, BookkeepingFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})



