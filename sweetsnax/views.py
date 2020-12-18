from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Order
from .forms import OrderForm
from .serializers import OrderSerializer
from rest_framework import generics 

# Create your views here.


@api_view(['GET'])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
  
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, pk):
    order = Order.objects.filter(email=pk)
    print(order)
    serializer = OrderSerializer(order, many=True)
    
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe = False)


# @api_view(['POST'])
# def orderCreate(request):
#     serializer = OrderSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class OrderLista(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 

@api_view(['PUT'])
def orderUpdate(request, pk):
    order = Order.objects.filter(email=pk)
    serializer = OrderSerializer(instance=order, data=request.data)
  

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(email=pk)
    order.delete()
    return Response(serializer.data)



