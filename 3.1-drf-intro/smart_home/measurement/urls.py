from django.urls import path

from measurement.views import UpdateSensor, GetOrCreateSensors, CreateMeasurement, GetMeasurements

urlpatterns = [
    path('sensors/', GetOrCreateSensors.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
    # path('measurements/<pk>/', GetMeasurements.as_view()),
]
