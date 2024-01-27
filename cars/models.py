from django.db import models


class Cars(models.Model):
    car_make = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50, default="")
    car_type = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/images")

    def __str__(self):
        return self.car_make