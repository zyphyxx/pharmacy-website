from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='images/products', blank=True, null=True)

    def __str__(self):
        return self.name
