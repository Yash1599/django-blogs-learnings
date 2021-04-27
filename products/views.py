from django.http import Http404
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
# Create your views here.
def product_detail_view(request ,id ):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context={
        'title' : obj.title,
    }
    return render(request , "product/detail.html" , context)

def product_delete_view(request , id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()

    context={
        'object' : obj,
    }
    return render(request , "product/delete.html" , context)

def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        'object_list' : queryset
    }
    return render(request , "product/delete.html" , context)

