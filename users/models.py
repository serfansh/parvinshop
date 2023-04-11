from django.db import models
from django.contrib.auth.models import User
import uuid

from store.models import Product



class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=200, null=True)
    receiver = models.CharField(max_length=200, null=True)
    postalcode = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                    primary_key=True, editable=False) 

    def __str__(self):
        return str(self.user.username) + ' ' + str(self.city)                    
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.IntegerField(null=True, blank=True, default=15000)
    totalPrice = models.IntegerField(null=True, blank=True, default=0)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)    
    
    def __str__(self):
        return str(self.user.username) + ' ' + str(self.totalPrice)

    class Meta:
        ordering = ['createdAt']


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.IntegerField()
    details = models.TextField(null=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)