from django.db import models
from django.urls import reverse
from datetime import date

REGIONS = (
    ('H', 'Hoenn'),
    ('K', 'Kanto'),
    ('J', 'Johto')
)

class Item(models.Model):
  name = models.CharField(max_length=50)
  types = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('items_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  items = models.ManyToManyField(Item)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'poke_id': self.id})

class Training(models.Model):
  date = models.DateField('training date')
  region = models.CharField(
    max_length=1,
    choices=REGIONS,
    default=REGIONS[0][0]
  )
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_region_display()} on {self.date}"

  class Meta:
    ordering = ['-date']