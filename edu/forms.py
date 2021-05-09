from functools import partial
from django import forms
from edu.models import EduEntryStatistics, EduEntryFileStatistics, EduEntryListenStatistics

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class EduEntryStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EduEntryStatistics
        fields = ['edu_entry', 'date_start', 'date_end']


class EduEntryFileStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EduEntryFileStatistics
        fields = ['edu_entry', 'date_start', 'date_end']


class EduEntryListenStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EduEntryListenStatistics
        fields = ['edu_entry', 'date_start', 'date_end']