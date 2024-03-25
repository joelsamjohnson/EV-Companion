from django.db import models



class ServiceCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    need_delivery_boy = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    service_center = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class DeliveryBoy(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"