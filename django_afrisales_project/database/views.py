from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Sales
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import SalesSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls ={
        'List':'/sales-list'
    }
    return Response(api_urls)

@api_view(['GET'])
def sales_list(request):
    sales = Sales.objects.all() 
    serializer = SalesSerializer(sales, many=True) 
    return Response(serializer.data) 

def index(request):
    return HttpResponse('JACOB ZUMA SE MA SE POES!')
