from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    #slug = models.SlugField(max_length=222, unique=True)

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
    # image = models.ImageField(upload_to='images/')
    # slug = models.SlugField(max_length=255)
    #in_stock?

class Meta:
    verbose_name_plural = 'Products'


# class User(models.Model):
#     pass
