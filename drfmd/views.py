from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Master, Detail
from .serializers import MasterSerializer, DetailSerializer
from .filters import DetailFilter

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    filterset_class = DetailFilter
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = {'master__name': ['exact', 'contains']}
