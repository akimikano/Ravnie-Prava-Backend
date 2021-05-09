from django.urls import path
from edu.views import EduHeadAPIView, EduEntryListAPIView, EduEntryDetailAPIView, LawyerListAPIView, \
    LawyerDetailAPIView, EntityListAPIView, DeptListAPIView, DeptDetailAPIView, CitiesListAPIView, \
    FileDownloadListAPIView, FileKgDownloadListAPIView, EduEntryListenedView, EduEntryListenedKgView, \
    EduEntryCheckedView, EduEntryDownloadedView, EduEntryDownloadedKgView, DeptCheckedView

urlpatterns = [
    path('', EduHeadAPIView.as_view(), name='edu_head'),
    path('<int:pk>', EduEntryListAPIView.as_view(), name='edu_entry'),
    path('entries/<int:pk>', EduEntryDetailAPIView.as_view(), name='edu_entry_detail'),
    path('entries/<int:id>/download', FileDownloadListAPIView.as_view(), name='edu_entry_download'),
    path('entries/<int:id>/kg/download', FileKgDownloadListAPIView.as_view(), name='edu_entry_download_kg'),

    path('entries/<int:id>/listened', EduEntryListenedView.as_view(), name='edu_entry_listened'),
    path('entries/<int:id>/kg/listened', EduEntryListenedKgView.as_view(), name='edu_entry_listened_kg'),

    path('entries/<int:id>/checked', EduEntryCheckedView.as_view(), name='edu_entry_checked'),
    path('entries/<int:id>/downloaded', EduEntryDownloadedView.as_view(), name='edu_entry_downloaded'),
    path('entries/<int:id>/kg/downloaded', EduEntryDownloadedKgView.as_view(), name='edu_entry_downloaded_kg'),

    path('lawyers/', LawyerListAPIView.as_view(), name='edu_lawyer'),
    path('lawyers/<int:pk>', LawyerDetailAPIView.as_view(), name='edu_lawyer_detail'),
    path('entities/', EntityListAPIView.as_view(), name='edu_entity'),
    path('<int:pk>/departments/', DeptListAPIView.as_view(), name='edu_department'),
    path('departments/<int:pk>', DeptDetailAPIView.as_view(), name='edu_department_detail'),

    path('departments/<int:id>/checked', DeptCheckedView.as_view(), name='edu_department_checked'),
    path('cities/', CitiesListAPIView.as_view(), name='edu_cities')
]

