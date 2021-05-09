from functools import partial
from django import forms
from base.models import EntryStatistics, EntryFileStatistics, EntryListenStatistics

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class EntryStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = EntryStatistics
        fields = ['entry', 'date_start', 'date_end']


class EntryFileStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = EntryFileStatistics
        fields = ['entry', 'date_start', 'date_end']


class EntryListenStatisticsForm(forms.ModelForm):
    date_start = forms.CharField(widget=DateInput(), required=False, label='Дата от')
    date_end = forms.CharField(widget=DateInput(), required=False, label='Дата до')

    class Meta:
        model = EntryListenStatistics
        fields = ['entry', 'date_start', 'date_end']