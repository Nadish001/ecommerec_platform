from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    des = models.TextField()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=30)
    des = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='products')
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name