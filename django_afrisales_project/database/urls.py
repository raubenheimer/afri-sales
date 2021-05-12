from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sales-list/', views.sales_list, name='sales-list'),
]