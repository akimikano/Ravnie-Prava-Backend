import io
import os
from wsgiref.util import FileWrapper
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from employment.models import Site, EmpSubhead, EmpEntryPhoto, EmpEntryAudio, Other, Course, EmpHead, \
    EmpEntryAudioStatistics, EmpEntryAudioStatisticsMonth, EmpEntryAudioFileStatisticsMonth, \
    EmpEntryAudioFileStatistics, EmpEntryAudioListenStatistics, EmpEntryAudioListenStatisticsMonth
from employment.serializers import EmpHeadSerializer, SiteSerializer, EmpSubheadSerializer, \
    EmpEntryPhotoListSerializer, EmpEntryAudioListSerializer, EmpEntryPhotoDetailSerializer, \
    EmpEntryAudioDetailSerializer, OtherSerializer, \
    CourseListSerializer, CourseDetailSerializer, OtherTypeSerializer, SiteTypeSerializer
from employment.utils import increment_downloads_count, increment_downloads_count_kg, increment_views_count
from vmeste.settings import STATICFILES_DIRS


class EmpHeadListAPIView(ListAPIView):
    """
    Главы раздела (список)

    1. Без id
    get - list

    """
    queryset = EmpHead.objects.all()
    serializer_class = EmpHeadSerializer


class SiteListAPIView(ListAPIView):
    """
    Сайты (список)

    1. Без id
    get - list

    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_queryset(self):
        queryset = Site.objects.all()
        for obj in queryset:
            if EmpSubhead.objects.filter(head=obj.head):
                queryset = queryset.exclude(id=obj.id)

        return queryset


@permission_classes((permissions.AllowAny,))
class EmpSubheadListAPIView(APIView):
    """
      Подглавы глав (список)

      1. Без id
      get - list

      """

    def get(self, request, pk):
        queryset = EmpSubhead.objects.filter(head=pk)
        serializer = EmpSubheadSerializer(queryset, many=True)
        print(serializer)
        data = serializer.data
        try:
            site = Site.objects.filter(head=pk)
            course_data = SiteTypeSerializer(site, many=True).data
            other = Other.objects.filter(head=pk)
            other_data = OtherTypeSerializer(other, many=True).data
            print(other_data)
            if course_data:
                for o in course_data:
                    data.append(o)
            if other_data:
                for o in other_data:
                    data.append(o)
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response(data, status=status.HTTP_201_CREATED)


@permission_classes((permissions.AllowAny,))
class EmpEntryPhotoListAPIView(APIView):
    """
    Статьи подглавы с документом (список)

    1. Без id
    get - list

    """
    def get(self, request, pk):
        queryset = EmpEntryPhoto.objects.filter(subhead=pk)
        serializer = EmpEntryPhotoDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmpEntryPhotoDetailAPIView(RetrieveAPIView):
    """
    Статья подглавы с документом (детально)

    1. C ID
    get - retrieve

    """
    queryset = EmpEntryPhoto.objects.all()
    serializer_class = EmpEntryPhotoDetailSerializer


@permission_classes((permissions.AllowAny,))
class EmpEntryAudioListAPIView(APIView):
    """
    Статьи подглавы (список)

    1. Без id
    get - list

    """
    def get(self, request, pk):
        queryset = EmpEntryAudio.objects.filter(subhead=pk)
        serializer = EmpEntryAudioDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmpEntryAudioDetailAPIView(RetrieveAPIView):
    """
    Статья подглавы (детально)

    1. C ID
    get - retrieve

    """
    queryset = EmpEntryAudio.objects.all()
    serializer_class = EmpEntryAudioDetailSerializer


class OtherAPIView(viewsets.ModelViewSet):
    """
    Др. информация (детально)

    1. Без ID
    get - retrieve

    """
    serializer_class = OtherSerializer
    queryset = Other.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class CourseListAPIView(APIView):
    """
    Курсы (список)

    1. Без id
    get - list

    """
    def get(self, request, pk):
        queryset = Course.objects.filter(subhead=pk)
        serializer = CourseDetailSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseDetailAPIView(RetrieveAPIView):
    """
    Курс (детально)

    1. С id
    get - retrieve

    """
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


@permission_classes((permissions.AllowAny,))
class FileDownloadListAPIView(APIView):
    """
    Скачать файл (резюме)

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        obj = EmpEntryPhoto.objects.get(id=id)
        file_handle = obj.photo.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % obj.photo.name
        return response


@permission_classes((permissions.AllowAny,))
class FileDownloadAudioListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = EmpEntryAudio.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


@permission_classes((permissions.AllowAny,))
class FileKgDownloadAudioListAPIView(APIView):
    """
    Скачать файл

    1. C ID
    get - retrieve

    """
    def get(self, request, id, format=None):
        queryset = EmpEntryAudio.objects.get(id=id)
        file_handle = queryset.file_kg.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file_kg.name
        return response


class EmpEntryListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(emp_entry_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(emp_entry_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EmpEntryListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(emp_entry_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(emp_entry_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EmpEntryCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioStatistics.objects.get(emp_entry_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioStatistics.objects.create(emp_entry_id=kwargs['id'])

        try:
            increment_views_count(statistics, EmpEntryAudioStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EmpEntryDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(emp_entry_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(emp_entry_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class EmpEntryDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(emp_entry_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(emp_entry_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


# courses
class CourseListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(course_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(course_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class CourseListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(course_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(course_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class CourseCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioStatistics.objects.get(course_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioStatistics.objects.create(course_id=kwargs['id'])

        try:
            increment_views_count(statistics, EmpEntryAudioStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class CourseDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(course_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(course_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class CourseDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(course_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(course_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


# listen
class ResumeListenedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(resume_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(resume_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class ResumeListenedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioListenStatistics.objects.get(resume_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioListenStatistics.objects.create(resume_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioListenStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class ResumeCheckedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioStatistics.objects.get(resume_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioStatistics.objects.create(resume_id=kwargs['id'])

        try:
            increment_views_count(statistics, EmpEntryAudioStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class ResumeDownloadedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(resume_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(resume_id=kwargs['id'])
        try:
            increment_downloads_count(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


class ResumeDownloadedKgView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        try:
            statistics = EmpEntryAudioFileStatistics.objects.get(resume_id=kwargs['id'])
        except:
            statistics = EmpEntryAudioFileStatistics.objects.create(resume_id=kwargs['id'])
        try:
            increment_downloads_count_kg(statistics, EmpEntryAudioFileStatisticsMonth)
            return Response(status=status.HTTP_200_OK, data={'success': True})
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data={'success': False})


def course_download(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    buffer = io.BytesIO()
    canvas = Canvas(buffer)
    pdfmetrics.registerFont(TTFont('Times', os.path.join(STATICFILES_DIRS[0], 'fonts', 'times.ttf')))
    canvas.setFont('Times', 26)
    canvas.drawString(200, 750, "Информация о курсе")
    canvas.setFont('Times', 15)
    canvas.drawString(50, 700, f"Категория: {obj.category}")
    canvas.drawString(50, 675, f"Описание: {obj.description}")
    canvas.drawString(50, 650, f"Название: {obj.name}")
    canvas.drawString(50, 625, f"Компания: {obj.company}")
    canvas.drawString(50, 575, f"Телефон: {obj.phone}")
    canvas.drawString(50, 600, f"Электронная почта: {obj.email}")
    canvas.drawString(50, 550, f"Адрес: {obj.address}")
    canvas.showPage()
    canvas.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'Курс_{obj.name}.pdf')
