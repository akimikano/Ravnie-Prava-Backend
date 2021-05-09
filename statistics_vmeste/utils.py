from datetime import date

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

def increment_mobile_statistics(statistics_model, downloads_model):
    datetime = date.today()
    month = datetime.month
    year = datetime.year

    if not statistics_model.objects.filter(date__month=month, date__year=year).exists():
        statistics = statistics_model.objects.create(date=f'{year}-{month}-01',
                                                     name=f'{months[month]}, {year}', total_count=1)
        downloads_model.objects.create(fk=statistics)
    else:
        statistics = statistics_model.objects.filter(date__year=year, date__month=month)
        statistics = statistics.first()
        statistics.total_count = statistics.total_count + 1
        statistics.save()
        downloads_model.objects.create(fk=statistics)