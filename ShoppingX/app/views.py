from django.shortcuts import render
from django.views import View
from .models import *
# def home(request):
#  return render(request, 'app/home.html')

class Productsviews(View):
 def get(self, request):
  topware=Product.objects.filter(catagory='TW')
  BottomWear=Product.objects.filter(catagory='BW')
  Laptop=Product.objects.filter(catagory='L')
  Mobile=Product.objects.filter(catagory='M')
  return render(request, 'app/home.html', context={'TopWear':topware, 'BottomWear':BottomWear, 'Laptop':Laptop, 'Mobile':Mobile})
 

  
  

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
 
class ProductDetails(View):
 def get(self,request,pk):
   product=Product.objects.get(pk=pk)
   return render(request, 'app/productdetail.html', context={'product':product})
  





def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    mobiles = None  # Initialize mobiles to None
    
    if data is None:
        mobiles = Product.objects.filter(catagory='M')
    elif data.lower() in ['redmi', 'xiaomi']:
        mobiles = Product.objects.filter(catagory='M', brand=data)
    elif data.lower() in ['samsung', 'galaxy']:
        mobiles = Product.objects.filter(catagory='M', brand=data)
    elif data.lower()=="realme":
        mobiles = Product.objects.filter(catagory='M', brand=data)
    elif data.lower()=="vivo":
        mobiles = Product.objects.filter(catagory='M', brand=data)
    elif data.lower()=="infinix":
        mobiles = Product.objects.filter(catagory='M', brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(catagory='M').filter(discount_price__lt=10000)
    elif data=='above':
        mobiles=Product.objects.filter(catagory='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})
def topwear(request, data=None):
    topwears = None  # Initialize mobiles to None
    if data is None:
        topwears = Product.objects.filter(catagory='TW')
    elif data=='puma':
        topwears = Product.objects.filter(catagory='TW', brand=data)
    elif data=='nike':
        topwears = Product.objects.filter(catagory='TW', brand=data)
    elif data=='below':
        topwears=Product.objects.filter(catagory='TW').filter(discount_price__lt=10000)
    elif data=='above':
        topwears=Product.objects.filter(catagory='TW').filter(discount_price__gt=10000)
    return render(request,'app/topwear.html', {'topwears': topwears})

def bottomwear(request, data=None):
    bottomwears = None  # Initialize mobiles to None
    if data is None:
        bottomwears = Product.objects.filter(catagory='BW')
    elif data=='puma':
        bottomwears = Product.objects.filter(catagory='BW', brand=data)
    elif data=='nike':
        bottomwears = Product.objects.filter(catagory='BW', brand=data)
    elif data=='below':
        bottomwears=Product.objects.filter(catagory='BW').filter(discount_price__lt=10000)
    elif data=='above':
        bottomwears=Product.objects.filter(catagory='BW').filter(discount_price__gt=10000)
    return render(request,'app/bottomwear.html', {'bottomwears': bottomwears})

def laptop(request, data=None):
    laptops = None  # Initialize mobiles to None
    
    if data is None:
        laptops = Product.objects.filter(catagory='L')
    elif data.lower()=='lenovo':
        laptops = Product.objects.filter(catagory='L', brand=data)
    elif data.lower()=='asus':
        laptops = Product.objects.filter(catagory='L', brand=data)
    elif data.lower()=="samsung":
        laptops = Product.objects.filter(catagory='L', brand=data)
    elif data.lower()=="hp":
        laptops = Product.objects.filter(catagory='L', brand=data)
    elif data=='below':
        laptops=Product.objects.filter(catagory='L').filter(discount_price__lt=10000)
    elif data=='above':
        laptops=Product.objects.filter(catagory='L').filter(discount_price__gt=10000)
    return render(request, 'app/laptop.html', {'laptop': laptops})


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
