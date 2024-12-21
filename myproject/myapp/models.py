from django.db import models

# Create your models here.
class Invoice(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=50,default="name")
    address=models.CharField(max_length=50, default="Default Address")
    phone=models.CharField(max_length=50,default="phone")
    price=models.CharField(max_length=50,default="price")
    total=models.CharField(max_length=78,default="total")
    description=models.TextField(default="Default description")


