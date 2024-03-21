from django.db import models
import uuid
# Create your models here.
class ChargingStation(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Example precision for latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Example precision for longitude
    address = models.CharField(max_length=200)
    operating_hours = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='charging_station_images/', null=True, blank=True)
    contact_info = models.CharField(max_length=100)
    operational_status = models.BooleanField(default=True)
    # Other fields for additional station details

    def __str__(self):
        return self.name