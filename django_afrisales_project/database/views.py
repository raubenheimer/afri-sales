from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Sales

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def sales_list(request):
    sales = Sales.objects.all() 
    context = {"sales": sales} 
    return render(request, 'app/sales_list.html', context) 
