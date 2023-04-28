from django.db.models import Q, F
from .models import Product, Csqp, Image, Color, Size
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Order


def searchProducts(request):
    search_query = ''
    clothes_for = ''
    categories = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    products = Product.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(category__icontains=search_query) |
        Q(clothes_for__icontains=search_query)
    )
    if request.POST.getlist('clothes_for'):
        clothes_for = request.POST.getlist('clothes_for')  
        products = products.filter(clothes_for__in=clothes_for)
        
    if request.GET.getlist('clothes_for'):
        clothes_for = request.GET.getlist('clothes_for')  
        products = products.filter(clothes_for__in=clothes_for)

    if request.POST.getlist('select-category'):
        categories = request.POST.getlist('select-category')
        products = products.filter(category__in=categories)

    return products, search_query, clothes_for, categories



def paginateProducts(request, products, results):
    
    page = request.GET.get('page')
    paginator = Paginator(products, results)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1   

    custom_range = range(leftIndex, rightIndex)

    return custom_range, products


def deletestuff(request):
    try:
        Csqp.objects.get(id=request.POST['csqpid']).delete()
    except:
        pass

    try:
        Image.objects.get(id=request.POST['imageid']).delete()
    except:
        pass


def deletecs(request):
    try:
        Color.objects.get(id=request.POST['colorid']).delete()
    except:
        pass
    
    try:
        Size.objects.get(id=request.POST['sizeid']).delete()
    except:
        pass



def getOrder(request):
    try:
        order = request.user.order_set.all()[0]
        if order.isPaid:
            raise Exception()
    except:
        order = Order.objects.create(user=request.user)
     
    if order:
        orderitems = order.orderitem_set.all()
    else:
        orderitems = None
    
    return order, orderitems