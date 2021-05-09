from django.urls import path
from base.views import EntryListAPIView, HeadAPIView, EntryDetailAPIView, FileDownloadListAPIView, \
    FileKgDownloadListAPIView, EntryListenedView, EntryListenedKgView, EntryFileDownloadedView, \
    EntryFileDownloadedKgView, EntryCheckedView
from django.conf.urls.static import static

from vmeste import settings

urlpatterns = [
    path('', HeadAPIView.as_view(), name='base_head'),
    path('<int:pk>', EntryListAPIView.as_view(), name='base_entry'),
    path('entries/<int:pk>', EntryDetailAPIView.as_view(), name='base_entry_detail'),
    path('entries/<int:id>/download', FileDownloadListAPIView.as_view(), name='base_entry_download'),
    path('entries/<int:id>/kg/download', FileKgDownloadListAPIView.as_view(), name='base_entry_download_kg'),

    path('entries/<int:id>/listened', EntryListenedView.as_view(), name='entry_listened'),
    path('entries/<int:id>/kg/listened', EntryListenedKgView.as_view(), name='entry_listened_kg'),

    path('entries/<int:id>/downloaded', EntryFileDownloadedView.as_view(), name='entry_downloaded'),
    path('entries/<int:id>/kg/downloaded', EntryFileDownloadedKgView.as_view(), name='entry_downloaded_kg'),

    path('entries/<int:id>/checked', EntryCheckedView.as_view(), name='entry_checked_kg'),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)