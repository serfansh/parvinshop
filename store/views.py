from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from users.models import OrderItem, Order
from .models import Product, Image, Color, Size, Csqp
from .forms import ProductForm, ImageForm, CsqpForm, ColorForm, SizeForm
from .utils import searchProducts, paginateProducts, deletestuff, deletecs, getOrder



def home(request):
    products = Product.objects.all()[:12]

    context = {'products': products, 'store': True}
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
        order, _ = getOrder(request)

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
    

@user_passes_test(lambda u: u.is_staff)
def addProduct(request):
    form = ProductForm()
    csqpform = CsqpForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        csqpform = CsqpForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            product = form.save()
            for image in images:
                Image.objects.create(product=product, image=image)

            if csqpform.is_valid():
                csqpform = csqpform.save(commit=False)
                csqpform.product = product
                csqpform.save() 

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


@user_passes_test(lambda u: u.is_staff)
def addColor(request):
    form = ColorForm()
    colors = Color.objects.all()

    if request.method == 'POST':
        deletecs(request)
        cform = ColorForm(request.POST)
        if cform.is_valid():
            cform.save()

    context = {'form': form, 'page': 'color', 'colors': colors}
    return render(request, 'store/addcolorsize.html', context)


@user_passes_test(lambda u: u.is_staff)
def addSize(request):
    form = SizeForm()
    sizes = Size.objects.all()

    if request.method == 'POST':
        deletecs(request)
        sform = SizeForm(request.POST)
        if sform.is_valid():
            sform.save()    

    context = {'form': form, 'sizes': sizes}
    return render(request, 'store/addcolorsize.html', context)