# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class GetOrCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.filter()
    serializer_class = SensorSerializer


class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class GetMeasurements(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        return Sensor.objects.filter(id=self.kwargs['pk'])
