from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Meta:
    verbose_name_plural = 'Products'



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)

