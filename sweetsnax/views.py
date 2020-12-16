from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Order
from .forms import OrderForm
from .serializers import OrderSerializer
from rest_framework import generics 
from rest_framework import permissions
# Create your views here.


@api_view(['GET'])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    permission_classes = (permissions.IsAuthenticated,)
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    permission_classes = (permissions.IsAuthenticated,)
    return Response(serializer.data)


# @api_view(['POST'])
# def orderCreate(request):
#     serializer = OrderSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class OrderLista(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

@api_view(['PUT'])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)
    permission_classes = (permissions.IsAuthenticated,)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    permission_classes = (permissions.IsAuthenticated,)
    return Response(serializer.data)



