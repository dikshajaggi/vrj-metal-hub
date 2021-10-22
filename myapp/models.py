from django.db import models

class Category (models.Model):
    category_id = models.AutoField
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='allProducts/')

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , default=1)
    image = models.ImageField(upload_to='allProducts/')
    color = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.email

class NewArrivals(models.Model):
    new_id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , default=1)
    image = models.ImageField(upload_to='newArivals/')
    color = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Offers(models.Model):
    offer_id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete = models.CASCADE , default=1)
    image = models.ImageField(upload_to='offers/')
    color = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name