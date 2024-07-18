from django.db import models

# Create your models here.


class CarModel(models.Model):
    model_nm=models.CharField(max_length=20)
    model_yr=models.CharField(max_length=20)
    description=models.CharField(max_length=20)

    def __str__(self):
        return self.model_nm

class Car(models.Model):
    car_nm=models.CharField(max_length=20)
    model=models.ManyToManyField(CarModel)

    def __str__(self):
        return self.car_nm