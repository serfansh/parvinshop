from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from users.models import OrderItem, Order
from .models import Product, Image, Color, Size, Csqp
from .forms import ProductForm, ImageForm, CsqpForm
from .utils import searchProducts, paginateProducts, deletestuff



def home(request):
    products = Product.objects.all()[:12]

    context = {'products': products}
    return render(request, 'store/store.html', context)


def products(request):
    products, search_query, clothes_for, categori = searchProducts(request)
    custom_range, products = paginateProducts(request, products, 16)
    categories = Product.objects.get_categories()
    colors = Color.objects.get_names()
    sizes = Size.objects.get_names()

    if request.method == "POST":
        print(request.POST)

        
    
    context = {'products': products, 'search_query': search_query,
     'custom_range': custom_range, 'clothes_for': clothes_for,
     'categories': categories, 'colors': colors, 'sizes': sizes,
     'categori': categori}
    return render(request, 'store/products.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    photos = product.image_set.all()
    csqp = product.csqp_set.all()

    if request.method == "POST":
        try:
            order = request.user.order_set.all()[0]
            if order.isPaid:
                raise Exception()
        except:
            order = Order.objects.create(user=request.user)
            
        for cs in request.POST.getlist('cs'):
            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=request.POST.get(cs),
                details=cs,
                price=product.price * int(request.POST.get(cs)),
                image=product.main_image.url
            )
            order.totalPrice += item.price
            order.save()

    context = {'product': product, 'photos': photos, 'csqp': csqp}
    return render(request, 'store/product.html', context)
    

def card(request):
    try:
        order = request.user.order_set.all()[0]
        if order.isPaid:
            raise Exception()
    except:
        order = None

    if order:
        orderitems = order.orderitem_set.all()
    else:
        orderitems = None
        
    address = request.user.useraddress
    
    if request.method == "POST":
        item = OrderItem.objects.get(id=request.POST.get('itemid'))
        order.totalPrice -= item.price
        item.delete()
        order.save()

    context = {'order': order, 'orderitems': orderitems, 'address': address}
    return render(request, 'store/card.html', context)


@user_passes_test(lambda u: u.is_staff)
def addProduct(request):
    form = ProductForm()
    csqpform = CsqpForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            for image in images:
                Image.objects.create(product=product, image=image)

            return redirect('product', product.id)

    context = {'form': form, 'csqpform': csqpform}
    return render(request, 'store/product_form.html', context)


@user_passes_test(lambda u: u.is_staff)
def editProduct(request, pk):
    product = Product.objects.get(id=pk)
    pics = product.image_set.all()
    form = ProductForm(instance=product)
    csqp = product.csqp_set.all()
    csqpform = CsqpForm()

    if request.method == "POST":
        deletestuff(request)
        csform = CsqpForm(request.POST)
        form = ProductForm(request.POST, request.FILES, instance=product)
        images = request.FILES.getlist('images')
        
        if csform.is_valid():
            cs = csform.save(commit=False)
            cs.product = product
            cs.save()

        if form.is_valid():
            product = form.save()
            for image in images:
                Image.objects.create(product=product, image=image)
            # return redirect('product', pk=product.id)

    context = {'form': form, 'page': 'edit', 'images': pics,
     'csqpform': csqpform, 'csqp': csqp}
    return render(request, 'store/product_form.html', context)


@user_passes_test(lambda u: u.is_staff)
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.delete()
        return redirect('home')

    context = {'product': product}
    return render(request, 'store/delete_product.html', context)

