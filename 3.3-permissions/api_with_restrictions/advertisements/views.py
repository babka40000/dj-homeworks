from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerDelete
from advertisements.serializers import AdvertisementSerializer


class MetricFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at']


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricFilter

    def get_permissions(self):
        """Получение прав для действий."""
        print(self.action)
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerDelete()]
        return []
