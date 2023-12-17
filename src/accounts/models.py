from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    STATUS = (
        ('Pending', 'pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivery', 'Delivery'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
