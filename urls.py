from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/', views.create_Order, name='create_order'),
    path('update_order/<str:pk>/', views.updateorder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order')





      
]
