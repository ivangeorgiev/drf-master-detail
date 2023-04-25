import django_filters
from .models import Detail

class DetailFilter(django_filters.FilterSet):
    master_name = django_filters.CharFilter(field_name='master__name', lookup_expr='icontains')

    class Meta:
        model = Detail
        fields = ['master_name']
