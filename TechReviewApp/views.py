from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review
# Create your views here.


def index(request):
    return render(request, 'TechReviewApp/index.html')


def getTypes(request):
    types_list = TechType.objects.all()
#name of the variable       #loads all objects from table to this list
    context={'types_list' : types_list}

    return render(request, 'TechReviewApp/types.html', context = context)


def getProducts(request):
    product_list = Product.objects.all()

    return render(request, 'TechReviewApp/products.html', {'product_list' : product_list})



def productsDetail(request, id):

    prod = Product.objects.get_object_or_404(pk=id)
    reviewcount = Review.objects.filter(product=id).count()
    reviews = Review.objects.filter(product=id)
    context = {
        'prod' : prod,
        'reviewcount' : count,
        'reviews' : reviews,
    }

    return render (request, 'TechReviewApp/productdetail.html', context=context)