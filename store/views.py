from django.shortcuts import render, get_object_or_404

from . models import Category , Product

def categories(request):
     return {
           'categories' :  Category.objects.all()
     }
            


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products' : products})

def product_detail(requset , slug):
      product = get_object_or_404(product, slug=slug, in_stock=True)
      return render(requset, 'store/product/detail.html',{'product': product})
      