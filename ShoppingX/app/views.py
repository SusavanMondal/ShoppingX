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

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
