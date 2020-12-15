from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Order
from .forms import OrderForm
from .serializers import OrderSerializer
# Create your views here.


@api_view(['GET'])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response(serializer.data)



