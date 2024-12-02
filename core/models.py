from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='default.png', upload_to='products/')
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    payment_preferences = models.CharField(max_length=50, default='PayPal')

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Process', 'In Process'),
        ('Cancelled', 'Cancelled'),
        ('Delivered', 'Delivered')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

from django.db import models

class Delivery(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ])
    estimated_delivery_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"Delivery for Order {self.order.id} - {self.status}"
