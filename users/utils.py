from django.contrib.auth.models import User
from .models import UserAddress, Order, OrderItem


def getAdress(user):
    try:
        address = user.useraddress
    except:
        address = None
    return address


def getLastOrder(user):
    try:
        order = user.order_set.latest('createdAt')
    except:
        order = None
    
    try:
        order_items = order.orderitem_set.all()
    except:
        order_items = None

    return order, order_items


def getAllOrders(user):
    try:
        orders = user.order_set.all()
    except:
        orders = None
    
    orders = [(order, order.orderitem_set.all()) for order in orders]

    return orders


def saveAddress(request, address):
    if not address:
        address = UserAddress.objects.create(
            user=request.user,
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            receiver=request.POST.get('receiver'),
            postalcode=request.POST.get('postalcode'),
        )

        try:
            address.clean_fields()
        except:
            address.delete()

    else:
        address.user = request.user
        address.city=request.POST.get('city')
        address.address=request.POST.get('address')
        address.phone=request.POST.get('phone')
        address.receiver=request.POST.get('receiver')
        address.postalcode=request.POST.get('postalcode')
        try:
            address.clean_fields()
            address.save()
        except:
            pass