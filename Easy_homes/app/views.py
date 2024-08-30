from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration, Product, Wishlist, Cart, Order, Category, Review, Architects_profile
from django.contrib.auth.models import User, auth
# Create your views here.

def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        data = Registration.objects.create_user(name=name, email=email, phone_number=phone_number, address=address, username=username, age=age, dob=dob, gender=gender, password=password, user_type="user")
        data.save()
        return redirect(login)
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        admin_user = auth.authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            auth.login(request, admin_user)
            return redirect(admin_home)
        data = auth.authenticate(username=username, password=password)
        if data is not None:
            auth.login(request, data)
            if data.user_type == "user":
                return redirect(home)
            elif data.user_type == "architect":
                return redirect(home)
            elif data.user_type == "seller" and data.status == "accept":
                return redirect(home)
            elif data.user_type == "seller" and data.status == "pending":
                return HttpResponse("can not login")
        else:
            return HttpResponse("invalid credentials")

    else:
        return render(request, 'login.html')
def seller_reg(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']
        data = Registration.objects.create_user(name=name, email=email, phone_number=phone_number, address=address,
                                                username=username, password=password, user_type="seller")
        data.save()
        return redirect(login)
    else:
        return render(request, 'seller_register.html')
def home(request):
    return render(request, 'homepage.html')
def admin_home(request):
    return render(request, 'adminhome.html')
def view_sellers(request):
    all = Registration.objects.filter(user_type="seller")
    return render(request, 'sellerslist.html', {'all': all})
def seller_details(request,id):
    view = Registration.objects.get(id=id)
    print(view)
    return render(request, 'sellers_details.html', {'view': view})
def seller_status(request, id):
    data = Registration.objects.get(id=id)
    print(data)
    if request.method == "POST":
        stat = request.POST['status']
        print(stat)
        try:
            if stat == "accept":
                data.status = stat
                data.save()
                return redirect(login)
            elif stat == "reject":
                data.status = stat
                data.save()
                return redirect(login)
            else:
                return HttpResponse("error")

        except Exception as e:
            return HttpResponse({e})
    else:
        # return render(request, 'sellerslist.html')
        return redirect(view_sellers)
def seller_options(request):
    return render(request, 'sellers_options.html')

# def pass_category(requet):
#     data = Category.objects.all()
#     return render()

def add_product(request):
    seller = Registration.objects.get(id=request.user.id)
    datas = Category.objects.all()
    # datas = Category.objects.get(id=category_id)
    if request.method == "POST":
        product_name = request.POST['product_name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        category = request.POST['category']
        categoryid = Category.objects.get(id=category)
        data = Product.objects.create(seller_id=seller, category_id=categoryid, product_name=product_name, price=price, description=description, image=image, category=category)
        data.save()

        return redirect(seller_options)
    else:
        return render(request, 'add_product.html', {'datas': datas})
def user_profile(request):
    data = Registration.objects.get(id=request.user.id)
    return render(request, 'userprofile.html', {'data': data})
def edit_userprofile(request):
    data = Registration.objects.get(id=request.user.id)
    if request.method == "POST":
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.age = request.POST['age']
        data.dob = request.POST['dob']
        data.gender = request.POST['gender']
        data.address = request.POST['address']
        data.save()
        return HttpResponse("edited")
    else:
        return render(request, 'edit_user.html', {'data': data})
def products_view(request):
    # data = Registration.objects.get()
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})
def product_details(request, product_id):
    details = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'details': details})
def my_products(request):
    # myproduct = Registration.objects.get(id=request.user.id)
    myproduct = Product.objects.filter(seller_id=request.user)
    return render(request,'my_products.html', {'myproduct': myproduct})

def seller_editproduct(request,id):
    data = Registration.objects.get(id=request.user.id)
    product = Product.objects.get(id=id)
    print(product)
    if request.method == "POST":
        product.product_name = request.POST['product_name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        print(data)
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect(my_products)
    else:
        return render(request, 'edit_products_seller.html', {'product': product})

def wishlist(request, id):
    # product = Product.objects.get(id=product_id)
    data = Registration.objects.get(id=request.user.id)
    product = Product.objects.get(id=id)
    datas = Wishlist.objects.create(product_id=product, user_id=data)
    datas.save()
    return redirect(wishlist_view)


def wishlist_view(request):
    # wishlist_items = Wishlist.objects.filter(user_id=request.user.id)
    wishlist_items = Wishlist.objects.all()
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def add_to_cart(request,id):
    cart = Registration.objects.get(id=request.user.id)
    cart_product = Product.objects.get(id=id)
    products = Product.objects.all()
    if Cart.objects.filter(product_id=cart_product, user_id=cart).exists():
        return render(request, 'view_products.html', {'msg':"Product already exists", 'products':products})
    else:
        datas = Cart.objects.create(product_id=cart_product, user_id=cart)
        datas.save()
        return redirect(view_cart)
def view_cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'view_cart.html', {'cart_items': cart_items})

def place_order(request):
    user = Registration.objects.get(id=request.user.id)
    cart_item = Cart.objects.filter(user_id=user)
    if request.method == "POST":
        payment_status = request.POST['payment_status']
    for i in cart_item:
        data = Order.objects.create(product_id=i.product_id, user_id=user, payment_status=payment_status)
        data.save()
    cart_item.delete()
    return redirect(order_confirmed)

def order_history(request):
    history = Order.objects.all()
    return render(request, 'customer_orders.html', {'history': history})

def remove_cart_item(request,id):
    user = Registration.objects.get(id=request.user.id)

    cart_items = Cart.objects.filter(id=id, user_id=user)
    cart_items.delete()
    return redirect(view_cart)
def delete_product(request,id):
    seller = Registration.objects.get(id=request.user.id)
    product = Product.objects.filter(id=id, seller_id=seller)
    product.delete()
    return redirect(my_products)
def add_category(request):
    if request.method == "POST":
        category_name = request.POST['category_name']
        data = Category.objects.create(category_name=category_name)
        data.save()
        return render(request, 'adminhome.html', {'add': "category added"})
    else:
        return render(request, 'adminhome.html')

# def view_category(request):
#     data = Product.objects.filter()

def logout(request):
    auth.logout(request)
    return redirect(login)

def customer_review(request,id):
    customer = Registration.objects.get(id=request.user.id)
    productid = Product.objects.get(id=id)
    if request.method == "POST":
        review = request.POST['review']
        date = request.POST['date']
        image = request.FILES['image']
        data = Review.objects.create(user_id=customer, product_id=productid, review=review, image=image, date=date)
        data.save()
        return HttpResponse("hf")
    else:
        return render(request, 'review.html')

# def payment(request):
#     customer = Registration.objects.get(id=request.user.id)
#
#     if request.method == "POST":
#         acc_number = request.POST['acc_number']
#         acc_holder = request.POST['acc_holder']
#         bank_name = request.POST['bank_name']
#         data = payment.objects.create(user_id=customer, cart_id=cart, acc_number=acc_number, acc_holder=acc_holder, bank_name=bank_name)
#         data.save()
#         return HttpResponse("payment successful")
#     else:
#         return render(request, 'payment_card.html')
# def payment_status(request):
#     # user = Registration.objects.get(id=request.user.id)
#     if request.method == "POST":
#         stat = request.POST['payment_status']
#
#         if stat == "paid":
#             payment_status =


def orderNow(request):
    return render(request, 'payment_card.html')

# def payment_status(request, id):
#     product = Product.objects.get(id=id)
#
#     if request.method == "POST":
#         payment_status = request.POST['payment_status']
#         data = Order.objects.create(product_id=product, payment_status=payment_status)
#         data.save()
#         return HttpResponse("ok")
#     else:
#         return render(request, 'payment_card.html')


def frontpage(request):
    return render(request, 'frontpage.html')

def arch_register(request):
    return render(request, 'architectRegister.html')

def search_product(request):
    if request.method == "POST":
        search_ = request.POST['search']
        data = Product.objects.filter(product_name__icontains=search_)
        return render(request, 'view_products.html', {'data': data})
    else:
        return render(request, 'view_products.html')


def arch_register(request):
    if request.method == "POST":
        name = request.POST['name']
        education = request.POST['education']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']
        data = Registration.objects.create_user(name=name, email=email, education=education, phone_number=phone_number, address=address,
                                                username=username, password=password, user_type="architect")
        data.save()
        return redirect(login)
    else:
        return render(request, 'architectRegister.html')

def createProfile_arch(request):
    arch = Registration.objects.get(id=request.user.id)
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        image2 = request.FILES['image2']
        project_scale = request.POST['project_scale']
        building_type = request.POST['building_type']
        model_type = request.POST['model_type']
        software = request.POST['software']
        data = Architects_profile.objects.create(architect_id=arch, name=name, price=price,
                        description=description, image=image, image2=image2, project_scale=project_scale, building_type=building_type, model_type=model_type, software=software)
        data.save()

        return redirect(viewArch)
    else:
        return render(request, 'createProfile_arch.html')

def viewArch(request):
    arch = Architects_profile.objects.all()
    return render(request, 'view_architects.html', {'arch': arch})

def search_arch(request):
    if request.method == "POST":
        search_ = request.POST['search']
        data = Architects_profile.objects.filter(name__icontains=search_)
        return render(request, 'view_architects.html', {'data': data})
    else:
        return render(request, 'view_architects.html')

def order_confirmed(request):
    return render(request, 'orderconfirmed.html')

