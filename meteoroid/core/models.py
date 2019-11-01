from django.db import models


class FIWAREBase(models.Model):
    fiware_service = models.CharField(max_length=64, default='', blank=True)
    fiware_service_path = models.CharField(max_length=64, default='/')

    class Meta:
        abstract = True


class Function(FIWAREBase):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.fiware_service}{self.fiware_service_path} {self.name}'

    class Meta:
        unique_together = ('name', 'fiware_service', 'fiware_service_path')
