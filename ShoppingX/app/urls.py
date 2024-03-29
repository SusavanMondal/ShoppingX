from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    # path('', views.home),
    path('',views.Productsviews.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetails.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),#fetch data for mobile
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),#fetch data for laptop
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),#fetch data for topwear
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),#fetch data for topwear
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),#login
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),#customerRegistration
    path('checkout/', views.checkout, name='checkout'),
    path('logout/',views.authlogout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
