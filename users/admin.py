from django.contrib import admin
from .models import Order, OrderItem, UserAddress



admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserAddress)