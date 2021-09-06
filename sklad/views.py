from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView

from rest_framework import generics
from .serializers import *


# Create your views here.


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductAPIListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()






def index(request, name):
    return render(request, "sklad/index.html", context={"name": name})


def products_list(request):
    products = Product.objects.all().order_by('name')
    title = 'List of Products'
    context = {
        'title': title,
        'products': products
    }
    return render(request, "sklad/product_list.html", context=context)


class ProductListView(ListView):
    model = Product
    template_name = 'sklad/product_list.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'kjdsgvjegvlqerhv;qerhvoqerhvoreqhi'
    }
