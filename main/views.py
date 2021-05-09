from rest_framework.generics import ListAPIView
from main.models import Section
from main.serializers import SectionSerializer


class SectionAPIView(ListAPIView):
    """
    Разделы (список)

    1. Без ID
    get - list

    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
