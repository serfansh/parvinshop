from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),
    path('addproduct/', views.addProduct, name='addproduct'),
    path('editproduct/<str:pk>/', views.editProduct, name='editproduct'),
    path('deleteproduct/<str:pk>/', views.deleteProduct, name='deleteproduct'),
    path('card/', views.card, name='card')
]

