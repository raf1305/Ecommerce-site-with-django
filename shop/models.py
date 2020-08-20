from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    date=models.DateField()
    category=models.CharField(max_length=20,default="Not available")
    subcategory=models.CharField(max_length=30,default="Not available")
    price=models.IntegerField(default=100)
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.name
        
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name