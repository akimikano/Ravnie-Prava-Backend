from functools import partial
from django import forms
from employment.models import EmpEntryAudioStatistics, EmpEntryAudioFileStatistics, EmpEntryAudioListenStatistics

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class EmpEntryAudioStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EmpEntryAudioStatistics
        fields = ['emp_entry', 'date_start', 'date_end']


class EmpEntryAudioFileStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EmpEntryAudioFileStatistics
        fields = ['emp_entry', 'date_start', 'date_end']


class EmpEntryAudioListenStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')
    views_count = forms.IntegerField(required=False, label='Всего просмотров')

    class Meta:
        model = EmpEntryAudioListenStatistics
        fields = ['emp_entry', 'date_start', 'date_end']