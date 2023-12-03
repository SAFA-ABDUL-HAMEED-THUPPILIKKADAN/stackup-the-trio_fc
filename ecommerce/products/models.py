from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name