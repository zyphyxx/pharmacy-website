from django.db import models


# Create your models here.
class Types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    types = models.ForeignKey(Types, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name
