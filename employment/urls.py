from django.urls import path
from employment.views import EmpHeadListAPIView, SiteListAPIView, EmpSubheadListAPIView, EmpEntryPhotoListAPIView, \
    EmpEntryPhotoDetailAPIView, EmpEntryAudioListAPIView, EmpEntryAudioDetailAPIView, OtherAPIView, CourseListAPIView, \
    CourseDetailAPIView, FileDownloadListAPIView, FileDownloadAudioListAPIView, course_download, \
    FileKgDownloadAudioListAPIView, EmpEntryListenedView, EmpEntryListenedKgView, EmpEntryCheckedView, \
    EmpEntryDownloadedView, EmpEntryDownloadedKgView, CourseCheckedView, CourseDownloadedView, CourseDownloadedKgView, \
    CourseListenedView, CourseListenedKgView, ResumeCheckedView, ResumeDownloadedView, ResumeDownloadedKgView, \
    ResumeListenedView, ResumeListenedKgView

urlpatterns = [
    path('', EmpHeadListAPIView.as_view(), name='employment_head'),
    path('sites/', SiteListAPIView.as_view(), name='employment_site'),
    path('<int:pk>/sub/', EmpSubheadListAPIView.as_view(), name='employment_subhead'),
    path('<int:pk>/resume/', EmpEntryPhotoListAPIView.as_view(), name='employment_photo'),
    path('<int:sub>/resume/<int:pk>', EmpEntryPhotoDetailAPIView.as_view(), name='employment_photo_detail'),
    path('resume/<int:id>/download', FileDownloadListAPIView.as_view(), name='employment_photo_download'),
    path('<int:pk>/entries/', EmpEntryAudioListAPIView.as_view(), name='employment_audio'),
    path('<int:sub>/entries/<int:pk>', EmpEntryAudioDetailAPIView.as_view(), name='employment_audio_detail'),
    path('entries/<int:id>/download', FileDownloadAudioListAPIView.as_view(), name='employment_audio_download'),
    path('entries/<int:id>/kg/download', FileKgDownloadAudioListAPIView.as_view(), name='employment_audio_download_kg'),

    path('entries/<int:id>/listened', EmpEntryListenedView.as_view(), name='employment_audio_listened'),
    path('entries/<int:id>/kg/listened', EmpEntryListenedKgView.as_view(), name='employment_audio_listened_kg'),

    path('entries/<int:id>/checked', EmpEntryCheckedView.as_view(), name='employment_audio_checked'),
    path('entries/<int:id>/downloaded', EmpEntryDownloadedView.as_view(), name='employment_audio_downloaded'),
    path('entries/<int:id>/kg/downloaded', EmpEntryDownloadedKgView.as_view(), name='employment_audio_downloaded_kg'),

    path('other/<int:pk>', OtherAPIView.as_view({'get': 'retrieve'}), name='employment_other'),
    path('<int:pk>/course/', CourseListAPIView.as_view(), name='employment_course'),
    path('course/<int:pk>', CourseDetailAPIView.as_view(), name='employment_course_detail'),
    path('course/<int:pk>/download', course_download, name='employment_course_download'),

    path('course/<int:id>/checked', CourseCheckedView.as_view(), name='employment_course_checked'),
    path('course/<int:id>/downloaded', CourseDownloadedView.as_view(), name='employment_course_downloaded'),
    path('course/<int:id>/kg/downloaded', CourseDownloadedKgView.as_view(), name='employment_course_downloaded_kg'),
    path('course/<int:id>/listened', CourseListenedView.as_view(), name='employment_course_listened'),
    path('course/<int:id>/kg/listened', CourseListenedKgView.as_view(), name='employment_course_listened_kg'),

    path('resume/<int:id>/checked', ResumeCheckedView.as_view(), name='employment_resume_checked'),
    path('resume/<int:id>/downloaded', ResumeDownloadedView.as_view(), name='employment_resume_downloaded'),
    path('resume/<int:id>/kg/downloaded', ResumeDownloadedKgView.as_view(), name='employment_resume_downloaded_kg'),
    path('resume/<int:id>/listened', ResumeListenedView.as_view(), name='employment_resume_listened'),
    path('resume/<int:id>/kg/listened', ResumeListenedKgView.as_view(), name='employment_resume_listened_kg'),
]
