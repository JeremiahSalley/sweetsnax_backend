from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('orders/<str:pk>/', views.order_detail, name='order_detail'),
    path('order/update/<str:pk>/', views.orderUpdate, name='orderUpdate'),
    path('order/delete/<str:pk>/', views.orderUpdate, name='orderDelete'),
        path('order/new', views.OrderLista.as_view(), name='orderCreate'),

]