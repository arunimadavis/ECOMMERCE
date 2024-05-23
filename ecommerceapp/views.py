from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
# Create your views here.
def allproducts(request,c_slug=None):
    c_page=None
    products_list=None
    paginator=Paginator([],6)
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
        paginator=Paginator(products_list ,6)
    try:
        page=int(request.GET.get('page','1'))
    except :
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

def searchresult(request):
    products=None
    query=None
    try:
        if 'q' in request.GET:
            query=request.GET.get('q')
            products=Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    except Exception as e:
        print(f"Error in searchresult view: {e}")
    return render(request,'search.html',{'query':query,'products':products})




