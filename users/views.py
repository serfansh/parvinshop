from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import UserAddress, Order, OrderItem
from .utils import getAdress, getLastOrder, getAllOrders, saveAddress, getOrder



def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created")

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error has occurred during registeration")

    context = {'form': form}
    return render(request, 'users/register.html', context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request,'username or password is not correct')

    return render(request, 'users/login.html',)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,'User was successfully logged out')
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):
    user = request.user
    address = getAdress(user)
    # order, order_items = getLastOrder(user)
    orders, ordders = getAllOrders(user)
    if request.method == 'POST':
        saveAddress(request, address)

    context = {'user': user, 'address': address, 
    'orders': orders, 'ordders': ordders}
    return render(request, 'users/account.html', context) 
 

@login_required(login_url='login')
def editUser(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        try:
            user.clean_fields()
            user.save()
        except:
            messages.error(request, 'Something Went Wrong!')

    return redirect('account')


@login_required(login_url='login')
def changePassword(request):

    if request.method == 'POST':
        user = request.user

        password = request.POST.get('password')
        new_password1 = request.POST.get('newpassword1')
        new_password2 = request.POST.get('newpassword2')

        if user.check_password(password):
            
            if new_password1 != new_password2:
                messages.error(request, 'باید رمز عبور جدید با تکرار رمز عبور مشابه باشند')
            else:
                user.set_password(new_password1)
                user.save()
        else:
            messages.error(request, 'رمز عبور اشتباه وارد شده')
        
    return render(request, 'users/change_password.html')


def card(request):
    order, orderitems = getOrder(request)

    address = request.user.useraddress
    
    if request.method == "POST":
        item = OrderItem.objects.get(id=request.POST.get('itemid'))
        order.totalPrice -= item.price
        item.delete()
        order.save()

    totalprice = order.totalPrice + order.shippingPrice

    context = {'order': order, 'orderitems': orderitems,
     'address': address, 'totalprice': totalprice}
    return render(request, 'users/card.html', context)
