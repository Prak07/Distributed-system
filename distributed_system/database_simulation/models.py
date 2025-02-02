from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta: 
        db_table = 'users'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

class Order(models.Model):
    user_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'orders'