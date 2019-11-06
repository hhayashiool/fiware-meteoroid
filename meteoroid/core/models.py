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


class Endpoint(FIWAREBase):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=64)
    method = models.CharField(max_length=8)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}{self.path} {self.function.name} {self.method}'

    class Meta:
        unique_together = ('name', 'path', 'method', 'fiware_service', 'fiware_service_path')


class Subscription(FIWAREBase):
    endpoint_id = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    orion_subscription_id = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.fiware_service}{self.fiware_service_path} {self.endpoint_id}'

    class Meta:
        unique_together = ('fiware_service', 'fiware_service_path')
