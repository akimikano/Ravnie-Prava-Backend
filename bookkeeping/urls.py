from django.urls import path
from bookkeeping.views import BookKeepingListAPIView, BookKeepingDetailAPIView, FileDownloadListAPIView, \
    FileKgDownloadListAPIView, BookkeepingListenedView, BookkeepingListenedKgView, BookkeepingCheckedView, \
    BookkeepingDownloadedView, BookkeepingDownloadedKgView

urlpatterns = [
    path('', BookKeepingListAPIView.as_view(), name='bookkeeping'),
    path('<int:pk>', BookKeepingDetailAPIView.as_view(), name='bookkeeping_detail'),
    path('<int:id>/download', FileDownloadListAPIView.as_view(), name='bookkeeping_download'),
    path('<int:id>/kg/download', FileKgDownloadListAPIView.as_view(), name='bookkeeping_download_kg'),

    path('<int:id>/listened', BookkeepingListenedView.as_view(), name='bookkeeping_listened'),
    path('<int:id>/kg/listened', BookkeepingListenedKgView.as_view(), name='bookkeeping_listened_kg'),

    path('<int:id>/checked', BookkeepingCheckedView.as_view(), name='bookkeeping_checked'),

    path('<int:id>/downloaded', BookkeepingDownloadedView.as_view(), name='bookkeeping_downloaded'),
    path('<int:id>/kg/downloaded', BookkeepingDownloadedKgView.as_view(), name='bookkeeping_downloaded_kg'),
]
