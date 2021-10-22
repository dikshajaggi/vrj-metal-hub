from django.shortcuts import render, HttpResponse
from .models import Product
from .models import Category
from .models import ContactForm
from .models import Offers
from .models import NewArrivals
# Create your views here.

def index(request):
    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()
    params = {
        'product':products,
        'category':categories
    }
    return render(request, 'myapp/index.html', params)

def prodCat (request):
    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()
    params = {
        'product':products,
        'category':categories
    }
    return render(request, 'myapp/prodCat.html',params)


def desc(request, id):
    product = Product.objects.filter(id=id).first()
    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()
    params = {
        'product':products,
        'product':product,
        'category':categories
    }
    return render(request, 'myapp/desc.html',params)

def form(request):
    if request.method == 'POST':
        contact = ContactForm(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            message = request.POST.get('message')
        )
        contact.save()

    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()
    params = {
        'product':products,
        'category':categories
    }

    return render(request , 'myapp/form.html' , params)

def about(request):
    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()
    params = {
        'product':products,
        'category':categories
    }
    return render(request , 'myapp/about.html' , params)

def offers(request):
    categories = Category.objects.all()
    offerProducts = Offers.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()

    
    params = {
        'product':products,
        'category':categories,
        'offers':offerProducts,
    }
    return render(request , 'myapp/offers.html' , params)

def newArrivals(request):
    categories = Category.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        products = Product.objects.filter(category = CATID)
    else:
        products = Product.objects.all()

    new = NewArrivals.objects.all()
    params = {
        'product':products,
        'category':categories,
        'newArrivals':new,
    }

    return render(request , 'myapp/newArrivals.html' , params)