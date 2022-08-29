from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']


class MeasurementSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer2(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']
