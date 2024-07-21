from django.shortcuts import render
from django.views import View
from .models import *
from .forms import CustomRegistrationFrom, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse



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
 user=request.user
 product_id=request.GET.get('prod_id')
 product=Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('showcart')
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        amount=0.0
        shippping_amount=0.0
        total_amount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
       
           
        if cart_product:
            for p in cart_product:
                temp_amount=(p.quantity*p.product.discount_price)
                amount+=temp_amount
            total_amount=amount+shippping_amount
    
            # print(carts.Product.items)
            return render(request, 'app/addtocart.html', {'carts': carts, 'total_amount':total_amount, 'amount':total_amount-70})
        else:
           return render(request, 'app/emptycart.html')
    else:
        return redirect('login')
    
def pluscart(request):
    if request.method=='GET':
      prod_id=request.GET['prod_id']

      c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      c.quantity+=1
      c.save()
      amount=0.0
      shippping_amount=0.0
      total_amount=0.0
      user = request.user
      cart_product = [p for p in Cart.objects.all() if p.user == user]
      for p in cart_product:
        temp_amount=(p.quantity*p.product.discount_price)
        amount+=temp_amount
        total_amount=amount
    data={
       'quantity':c.quantity,
       'amount':amount,
       'totalamount':total_amount+shippping_amount
        }
    return JsonResponse(data)
   
def minuscart(request):
   if request.method=='GET':
    prod_id=request.GET['prod_id']
    # print(prod_id)
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount=0.0
    shippping_amount=0.0
    total_amount=0.0
    user = request.user
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    # print(cart_product)
    for p in cart_product:
        temp_amount=(p.quantity*p.product.discount_price)
        amount+=temp_amount
        total_amount=amount
    data={
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':total_amount+shippping_amount,
    }
    return JsonResponse(data)
    

def remove_cart(request):
   if request.method=='GET':
    prod_id=request.GET['prod_id']
    # print(prod_id)
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount=0.0
    shippping_amount=0.0
    total_amount=0.0
    user = request.user
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    # print(cart_product)
    for p in cart_product:
        temp_amount=(p.quantity*p.product.discount_price)
        amount+=temp_amount
        total_amount=amount
    data={
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':total_amount+shippping_amount,
    }
    return JsonResponse(data)
    

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')
class ProfileView(View):
 def get(self, request):
    form=CustomerProfileForm()
    return render(request,'app/profile.html', context={'form':form, 'active':'btn-primary'})
 def post(self, request):
    form=CustomerProfileForm(request.POST)
    if form.is_valid():
       usr=request.user
       name=form.cleaned_data['name']
       locality=form.cleaned_data['locality']
       city=form.cleaned_data['city']
       state=form.cleaned_data['state']
       zip_code=form.cleaned_data['zip_code']
       reg=Customer(user=usr, name=name, locality=locality, city=city, state=state, zip_code=zip_code)
       reg.save()
       messages.success(request, ' Profile Updated Successfully!!')
    return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})
 





def address(request):
 add=Customer.objects.filter(user=request.user)
 

 return render(request, 'app/address.html', context={'add': add, 'active':'btn-primary'})


def orders(request):
 op=OrderPlace.objects.filter(user=request.user)
 return render(request, 'app/orders.html', context={'order_placed': op})


# def change_password(request):
#  return render(request, 'app/changepassword.html')

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


# def login(request):
#  return render(request, 'app/login.html')



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
   def get(self,request):
      form=CustomRegistrationFrom()
      return render(request,'app/customerregistration.html' , context={'form':form})
   def post(self,request):
      form=CustomRegistrationFrom(request.POST)
      if form.is_valid():
         messages.success(request, 'Successfully Registered!')
         form.save()
      return render(request,'app/customerregistration.html' , context={'form':form})


def authlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')
def checkout(request):
 user=request.user
 add=Customer.objects.filter(user=user)
 cart_item=Cart.objects.filter(user=user)
 amount=0.0
 shippping_amount=0.0
 total_amount=0.0
 
 cart_product = [p for p in Cart.objects.all() if p.user == user]
 if cart_product:   
    for p in cart_product:
        temp_amount=(p.quantity*p.product.discount_price)
        amount+=temp_amount
        total_amount=amount
 return render(request, 'app/checkout.html', {'add':add, 'totalamount':total_amount+70, 'cart_items':cart_item})


def payment_done(request):
   user=request.user
   custid=request.GET.get('custid')
   customer=Customer.objects.get(id=custid)
   cart=Cart.objects.filter(user=user)
   for c in cart:
      OrderPlace(user=user, customer=customer,product=c.product, quantity=c.quantity).save()
      c.delete()
   return redirect('orders')
