from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from edu.models import EduHead, EduEntry, Lawyer, Entity, Dept, City, EduEntryStatistics, EduEntryStatisticsMonth, \
    EduEntryFileStatisticsMonth, EduEntryFileStatistics, EduEntryListenStatistics, EduEntryListenStatisticsMonth
from edu.serializers import EduHeadSerializer, EduEntryListSerializer, EduEntryDetailSerializer, LawyerDetailSerializer, \
    EntitySerializer, DeptListSerializer, DeptDetailSerializer, LawyerListSerializer, CitySerializer
from employment.utils import increment_downloads_count_kg, increment_downloads_count, increment_views_count


class EduHeadAPIView(ListAPIView):
    """
    Главы раздела (список)

    1. Без id
    get - list

    """
    queryset = EduHead.objects.all()
    serializer_class = EduHeadSerializer


@permission_classes((permissions.AllowAny,))
class EduEntryListAPIView(APIView):
    """
    Статьи главы (список)

    1. Без ID
    get - list

    """

    def get(self, request, pk):
        queryset = EduEntry.objects.filter(head=pk)
        serializer = EduEntryDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EduEntryDetailAPIView(RetrieveAPIView):
    """
    Статья раздела (детально)

    api/likbez/{id главы}/entries/{id}

    1. C ID
    get - retrieve

    """
    queryset = EduEntry.objects.all()
    serializer_class = EduEntryDetailSerializer


class LawyerListAPIView(ListAPIView):
    """
    Юристы (список)

    1. Без ID
    get - list

    """
    queryset = Lawyer.objects.all()
    serializer_class = LawyerListSerializer


class LawyerDetailAPIView(RetrieveAPIView):
    """
    Юрист (детально)

    1. C ID
    get - retrieve

    """
    queryset = Lawyer.objects.all()
    serializer_class = LawyerDetailSerializer


class EntityListAPIView(ListAPIView):
    """
    Статьи главы (список)

    1. Без ID
    get - list

    """
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class CitiesListAPIView(ListAPIView):
    """
    Города (список)

    1. Без ID
    get - list

    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


@permission_classes((permissions.AllowAny,))
class DeptListAPIView(APIView):
    """
    Отделы организации (список с фильтром)

    api/likbez/{id организации}/departments?city=

    1. Без ID
    get - list

    """

    def get(self, request, pk):
        get_data = request.query_params
        if get_data:
            if get_data['city'] == '0':
                queryset = Dept.objects.filter(entity=pk)
            else:
                queryset = Dept.objects.filter(entity=pk, city=get_data['city'])
        else:
            queryset = Dept.objects.filter(entity=pk)
        serializer = DeptDetailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeptDetailAPIView(RetrieveAPIView):
    """
    Отдел организации (детально)

    api/likbez/{id организации}/departments/{id}

    1. C ID
    get - retrieve

    """
    queryset = Dept.objects.all()
    serializer_class = DeptDetailSerializer


@permission_classes((permissions.AllowAny,))
class FileDownloadListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = EduEntry.objects.get(id=id)
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
        queryset = EduEntry.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


class EduEntryListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryListenStatistics.objects.get(edu_entry_id=kwargs['id'])
        except:
            statistics = EduEntryListenStatistics.objects.create(edu_entry_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, EduEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EduEntryListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryListenStatistics.objects.get(edu_entry_id=kwargs['id'])
        except:
            statistics = EduEntryListenStatistics.objects.create(edu_entry_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EduEntryListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EduEntryCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryStatistics.objects.get(edu_entry_id=kwargs['id'])
        except:
            statistics = EduEntryStatistics.objects.create(edu_entry_id=kwargs['id'])
        try:
            increment_views_count(statistics, EduEntryStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EduEntryDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryFileStatistics.objects.get(edu_entry_id=kwargs['id'])
        except:
            statistics = EduEntryFileStatistics.objects.create(edu_entry_id=kwargs['id'])

        try:
            increment_downloads_count(statistics, EduEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EduEntryDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryFileStatistics.objects.get(edu_entry_id=kwargs['id'])
        except:
            statistics = EduEntryFileStatistics.objects.create(edu_entry_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EduEntryFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class DeptCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EduEntryStatistics.objects.get(dept_id=kwargs['id'])
        except:
            statistics = EduEntryStatistics.objects.create(dept_id=kwargs['id'])
        try:
            increment_views_count(statistics, EduEntryStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


