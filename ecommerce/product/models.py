from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class User(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

