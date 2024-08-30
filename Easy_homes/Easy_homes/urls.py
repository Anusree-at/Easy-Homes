"""
URL configuration for Easy_homes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg', views.registration),
    path('log', views.login),
    path('sellerreg', views.seller_reg),
    path('home', views.home),
    path('homeadmin', views.admin_home),
    path('sellers', views.view_sellers),
    path('view_details/<int:id>', views.seller_details, name="view_details"),
    path('status/<int:id>', views.seller_status, name="status"),
    path('becomeseller', views.seller_options),
    path('addproduct', views.add_product),
    path('userprofile', views.user_profile),
    path('edituser', views.edit_userprofile),
    path('viewproducts', views.products_view),
    path('viewmore/<int:product_id>', views.product_details, name="viewmore"),
    path('myproducts', views.my_products),
    path('editproduct/<int:id>', views.seller_editproduct, name="editproduct"),
    path('wishlist/<int:id>', views.wishlist, name="wishlist"),
    path('view_wishlist', views.wishlist_view, name="view_wishlist"),
    path('addtocart/<int:id>', views.add_to_cart, name="addtocart"),
    path('viewcart', views.view_cart),
    path('order', views.place_order, name="order"),
    path('orderhistory', views.order_history, name="orderhistory"),
    path('removecartitem/<int:id>', views.remove_cart_item, name="removecartitem"),
    path('dltproduct/<int:id>', views.delete_product, name="dltproduct"),
    path('category', views.add_category, name="category"),
    path('logout', views.logout, name="logout"),
    path('addreview', views.customer_review),
    path('paying', views.orderNow),
    path('', views.frontpage),
    path('archReg', views.arch_register),
    path('Search', views.search_product, name="Search"),
    path('viewarch', views.viewArch),
    path('createArch_profile', views.createProfile_arch),
    path('searchArch', views.search_arch),
    path('confirm', views.order_confirmed),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)