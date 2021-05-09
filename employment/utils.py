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

def increment_downloads_count(statistics, month_model):
    """
    Метод используется для повышения количества скачиваний а также прослушиваний
    """
    datetime = date.today()
    month = datetime.month
    year = datetime.year

    if month_model.objects.filter(fk=statistics, date__month=month, date__year=year).exists():
        month_statistics = month_model.objects.filter(fk=statistics, date__month=month, date__year=year)
        month_statistics = month_statistics.first()
        month_statistics.count = month_statistics.count + 1
        month_statistics.save()
    else:
        month_model.objects.create(fk=statistics, date=f'{year}-{month}-01', name=f'{months[month]}, {year}', count=1)


def increment_downloads_count_kg(statistics, month_model):
    """
    Метод используется для повышения количества скачиваний а также прослушиваний
    """
    datetime = date.today()
    month = datetime.month
    year = datetime.year

    if month_model.objects.filter(fk=statistics, date__month=month, date__year=year).exists():
        month_statistics = month_model.objects.filter(fk=statistics, date__month=month, date__year=year)
        month_statistics = month_statistics.first()
        month_statistics.count_kg = month_statistics.count_kg + 1
        month_statistics.save()
    else:
        month_model.objects.create(fk=statistics, date=f'{year}-{month}-01', name=f'{months[month]}, {year}',
                                   count_kg=1)


def increment_views_count(statistics, month_model):
    datetime = date.today()
    month = datetime.month
    year = datetime.year

    if month_model.objects.filter(fk=statistics, date__month=month, date__year=year).exists():
        month_statistics = month_model.objects.filter(fk=statistics, date__month=month, date__year=year)
        month_statistics = month_statistics.first()
        month_statistics.count = month_statistics.count + 1
        month_statistics.save()
        statistics.total_views = statistics.total_views + 1
        statistics.save()
    else:
        month_model.objects.create(fk=statistics, date=f'{year}-{month}-01', name=f'{months[month]}, {year}', count=1)
        statistics.total_views = statistics.total_views + 1
        statistics.save()