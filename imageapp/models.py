from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255,null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to="images/", null=True)

