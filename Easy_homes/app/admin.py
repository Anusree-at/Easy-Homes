from django.contrib import admin
from .models import Registration
from .models import Product
from .models import Category
from .models import Wishlist, Cart, Order, Review, Architects_profile
# Register your models here.


admin.site.register(Registration)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Architects_profile)

