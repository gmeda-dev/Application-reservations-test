import uuid
from django.db import models

# Create your models here.
class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Reservation(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255)
    date_check_in = models.DateField()
    date_check_out = models.DateField()
    rental = models.ForeignKey(Rental, on_delete=models.PROTECT)