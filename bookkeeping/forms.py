from functools import partial
from django import forms
from bookkeeping.models import BookkeepingStatistics, BookkeepingFileStatistics, BookkeepingListenStatistics

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class BookkeepingStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = BookkeepingStatistics
        fields = ['bookkeeping', 'date_start', 'date_end']


class BookkeepingFileStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = BookkeepingFileStatistics
        fields = ['bookkeeping', 'date_start', 'date_end']


class BookkeepingListenStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = BookkeepingListenStatistics
        fields = ['bookkeeping', 'date_start', 'date_end']


