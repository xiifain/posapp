from django.contrib.postgres.fields import ArrayField
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = ArrayField(models.CharField(max_length=50), blank =True)
    
    def __str__(self):
        return self.name
        
class Shop(models.Model):
    name = models.CharField(max_length=200)
    shopID = models.IntegerField()
    productIDs = models.ManyToManyField(Product, related_name="product_id")

    class Meta:
        managed = True

    def __str__(self):
        return f'{self.name}.{self.shopID}'




        
