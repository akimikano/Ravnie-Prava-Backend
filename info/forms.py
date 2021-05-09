from functools import partial
from django import forms
from info.models import InfoEntryStatistics, InfoEntryFileStatistics, InfoEntryListenStatistics

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class InfoEntryStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = InfoEntryStatistics
        fields = ['info_entry', 'date_start', 'date_end']


class InfoEntryFileStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = InfoEntryFileStatistics
        fields = ['info_entry', 'date_start', 'date_end']


class InfoEntryListenStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = InfoEntryListenStatistics
        fields = ['info_entry', 'date_start', 'date_end']

