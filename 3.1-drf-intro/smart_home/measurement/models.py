from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.title


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
