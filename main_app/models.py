from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CARES = (
  ('W', 'Water'),
  ('F', 'Fertilizer'),
  ('M', 'Mist')
)

class Plant(models.Model):
  name = models.CharField(max_length=100)
  location = models.TextField(max_length=250)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("plant-detail", kwargs={"plant_id": self.id})
  
class Caring(models.Model):
  date = models.DateField()
  care = models.CharField(
    'Care Given',
    max_length=1,
    choices=CARES,
    default=CARES[0][0],
  )
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_care_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']