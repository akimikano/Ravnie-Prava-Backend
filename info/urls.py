from django.urls import path

from info.views import InfoHeadAPIView, NewsListAPIView, NewsDetailAPIView, InfoSubheadListAPIView, \
    InfoEntryListAPIView, InfoEntryDetailAPIView, FileDownloadListAPIView, MediaDownloadListAPIView, \
    FileKgDownloadListAPIView, MediaKgDownloadListAPIView, InfoEntryListenedView, InfoEntryListenedKgView, \
    InfoEntryCheckedView, InfoEntryDownloadedView, InfoEntryDownloadedKgView, NewCheckedView, NewDownloadedView, \
    NewDownloadedKgView, NewListenedView, NewListenedKgView

urlpatterns = [
    path('', InfoHeadAPIView.as_view(), name='info_head'),
    path('media/', NewsListAPIView.as_view(), name='info_media'),
    path('media/<int:pk>', NewsDetailAPIView.as_view(), name='info_media_detail'),
    path('media/<int:id>/download', MediaDownloadListAPIView.as_view(), name='info_media_download'),
    path('media/<int:id>/kg/download', MediaKgDownloadListAPIView.as_view(), name='info_media_download_kg'),
    path('subhead/', InfoSubheadListAPIView.as_view(), name='info_subhead'),
    path('<int:pk>/publications/', InfoEntryListAPIView.as_view(), name='info_pub'),
    path('publications/<int:pk>', InfoEntryDetailAPIView.as_view(), name='info_pub_detail'),
    path('publications/<int:id>/download', FileDownloadListAPIView.as_view(), name='info_entry_download'),
    path('publications/<int:id>/kg/download', FileKgDownloadListAPIView.as_view(), name='info_entry_download_kg'),

    path('publications/<int:id>/checked', InfoEntryCheckedView.as_view(), name='info_entry_checked'),
    path('publications/<int:id>/downloaded', InfoEntryDownloadedView.as_view(), name='info_entry_downloaded'),
    path('publications/<int:id>/kg/downloaded', InfoEntryDownloadedKgView.as_view(), name='info_entry_downloaded_kg'),
    path('publications/<int:id>/listened', InfoEntryListenedView.as_view(), name='info_entry_listened'),
    path('publications/<int:id>/kg/listened', InfoEntryListenedKgView.as_view(), name='info_entry_listened_kg'),

    path('news/<int:id>/checked', NewCheckedView.as_view(), name='info_news_checked'),
    path('news/<int:id>/downloaded', NewDownloadedView.as_view(), name='info_news_downloaded'),
    path('news/<int:id>/kg/downloaded', NewDownloadedKgView.as_view(), name='info_news_downloaded_kg'),
    path('news/<int:id>/listened', NewListenedView.as_view(), name='info_news_listened'),
    path('news/<int:id>/kg/listened', NewListenedKgView.as_view(), name='info_news_listened_kg'),
]
