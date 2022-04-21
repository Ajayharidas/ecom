import os
from django.shortcuts import redirect, render
from ecomApp.models import Brand, Category,Product, Profile,ProductImages,Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate


def base(request):
    return render(request,'base.html',{})
# ---------- Add Category --------------
def add_category(request):
    if "uid" in request.session:
        if request.method == 'POST':
            cat_name = request.POST['cat_name']
            cat_image = request.FILES.get('cat_image')
            category = Category(category_name=cat_name,category_image=cat_image)
            category.save()
            return redirect('show_category')
        return render(request,'category/add_category.html',{})
    else:
        return redirect('log_in')

# --------------- Add Brand ---------------    
def add_brand(request):
    if "uid" in request.session:
        if request.method == 'POST':
            brand_name = request.POST['brand_name']
            brand_image = request.FILES.get('brand_image')
            brand = Brand(brand_name=brand_name,brand_image=brand_image)
            brand.save()
            messages.info(request,'Brand added successfully')
        return render(request,'brand/add_brand.html',{})
    else:
        return redirect('log_in')

# ------------------- Add product ---------------
def add_product(request):
    if "uid" in request.session:
        category = Category.objects.all()
        brand = Brand.objects.all()
        context = {'category':category,'brand':brand}
        if request.method == 'POST':
            pro_name = request.POST['pro_name']
            pro_price = request.POST['pro_price']
            pro_image = request.FILES.get('pro_image')
            br = request.POST['brand']
            brand = Brand.objects.get(id=br)
            cat = request.POST['category']
            category = Category.objects.get(id=cat)
            product = Product(product_name=pro_name,product_price=pro_price,product_image=pro_image,brand=brand,category=category)
            product.save()
            return redirect('product_table')
        return render(request,'product/add_product.html',context)
    else:
        return redirect('log_in')

# ------------ add multiple product images--------------

def add_multiple(request):
    if "uid" in request.session:
        product = Product.objects.all()
        if request.method == 'POST':
            pname = request.POST['product']
            pro = Product.objects.get(id=pname)
            images = request.FILES.getlist('images')
            for image in images:
                multi = ProductImages(images=image,product=pro)
                multi.save()
        return render(request,'product/add_multiple.html',{'product':product})
    else:
        return redirect('log_in')

# ------------ edit brand -------------

def edit_brand(request,pk):
    if "uid" in request.session:
        if request.method == 'POST':
            brand = Brand.objects.get(id=pk)
            brand.brand_name = request.POST['brand_name']
            if len(request.FILES) != 0:
                if len(brand.brand_image) > 0:
                    os.remove(brand.brand_image.path)
                brand.brand_image = request.FILES['brand_image']
            brand.save()
            return redirect('show_brand')
        brand = Brand.objects.get(id=pk)
        context = {'brand':brand}
        return render(request,'brand/edit_brand.html',context)

# ------------edit category ------------    
def edit_category(request,pk):
    if "uid" in request.session:
        if request.method == 'POST':
            category = Category.objects.get(id=pk)
            category.category_name = request.POST['cat_name']
            if len(request.FILES) != 0:
                if len(category.category_image) > 0:
                    os.remove(category.category_image.path)
                category.category_image = request.FILES['cat_image']
            category.save()
            return redirect('show_category')
        category = Category.objects.get(id=pk)
        context = {'category':category}
        return render(request,'category/edit_category.html',context)

# ------------ edit product -------------
def edit_product(request,pk):
    if "uid" in request.session:
        if request.method == 'POST':
            product = Product.objects.get(id=pk)
            product.product_name = request.POST['pro_name']
            product.product_price = request.POST['pro_price']
            brand = request.POST['brand']
            product.brand = Brand.objects.get(id=brand)
            category = request.POST['category']
            product.category = Category.objects.get(id=category)
            if len(request.FILES) != 0:
                if len(product.product_image) > 0:
                    os.remove(product.product_image.path)
                product.product_image = request.FILES['brand_image']
            product.save()
            return redirect('product_table')
        product = Product.objects.get(id=pk)
        brand = Brand.objects.all()
        category = Category.objects.all()
        context = {'product':product,'brand':brand,'category':category}
        return render(request,'product/edit_product.html',context)

# ----------------- delete brand ---------------

def delete_brand(request,pk):
    if "uid" in request.session:
        brand = Brand.objects.get(id=pk)
        brand.delete()
        return redirect('show_brand')

# ----------------- delete category ---------------

def delete_category(request,pk):
    if "uid" in request.session:
        category = Category.objects.get(id=pk)
        category.delete()
        return redirect('show_category')


# ----------------- delete product ---------------

def delete_product(request,pk):
    if "uid" in request.session:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('show_category')


# -------------- category table---------------
def show_category(request):
    if "uid" in request.session:
        category = Category.objects.all()
        context = {'category':category}
        return render(request,'category/show_category.html',context)

# -------------- brand table --------------------

def show_brand(request):
    if "uid" in request.session:
        brands = Brand.objects.all()
        return render(request,'brand/show_brand.html',{'brands':brands})

# --------------- product table -------------

def product_table(request):
    if "uid" in request.session:
        products = Product.objects.all()
        return render(request,'product/product_table.html',{'products':products}) 

# ----------------- show products -------------
def show_product(request,pk):
    if request.method == 'POST':
        if request.POST['brand'] is not None:
            brand = request.POST['brand']
            b_products = Product.objects.filter(brand=brand)
            brands = Brand.objects.all()
            category = Category.objects.all()
            context = {'b_products':b_products,'brands':brands,'category':category}
            return render(request,'product/brand_product.html',context)
        elif request.POST['category'] is not None:
            category = request.POST['category']
            c_products = Product.objects.filter(category=category)
            brands = Brand.objects.all()
            category = Category.objects.all()
            context = {'c_products':c_products,'brands':brands,'category':category}
            return render(request,'product/category_product.html',context)
        else:
            pass
    products = Product.objects.filter(category=pk)
    brands = Brand.objects.all()
    categs = Category.objects.all()
    context = {'products':products,'brands':brands,'categs':categs}
    return render(request,'product/show_product.html',context)

# ------------ show product brand wise ---------------
def brand_product(request):
    if request.method == 'POST':
        if request.POST['brand'] is not None:
            brand = request.POST['brand']
            b_products = Product.objects.filter(brand=brand)
            brands = Brand.objects.all()
            category = Category.objects.all()
            context = {'b_products':b_products,'brands':brands,'category':category}
            return render(request,'product/brand_product.html',context)
        else:
            messages.info(request,("You haven't selected anything..."))
            return redirect('brand_product')
    brands = Brand.objects.all()
    category = Category.objects.all()
    # b_name =  Brand.objects.filter(id=b_products)
    context = {'brands':brands,'category':category}
    return render(request,'product/brand_product.html',context)


# ------------ show product category wise -----------
def category_product(request):
    if request.method == 'POST':
        category = request.POST['category']
        c_products = Product.objects.filter(category=category)
        brands = Brand.objects.all()
        category = Category.objects.all()
        context = {'c_products':c_products,'brands':brands,'category':category}
        return render(request,'product/category_product.html',context)
    brands = Brand.objects.all()
    category = Category.objects.all()
    # b_name =  Brand.objects.filter(id=b_products)
    context = {'brands':brands,'category':category}
    return render(request,'product/category_product.html',context)

# ------------ show all products------------- 
def show_all(request):
    brands = Brand.objects.all()
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'products':products,'brands':brands,'category':category}
    return render(request,'product/show_all.html',context)

# ------------ show product details------------
def product_details(request,pk):
    details = Product.objects.get(id=pk)
    images = ProductImages.objects.filter(product=pk)
    return render(request,'product/product_details.html',{'details':details,'images':images})



# -----------signup------------
def sign_up(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        address = request.POST['address']
        email = request.POST['email']
        contact = request.POST['contact']
        uname = request.POST['uname']
        passw = request.POST['passw']
        cpassw = request.POST['cpassw']
        image = request.FILES.get('image')
        if passw == cpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists...')
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists...')
                return redirect('sign_up')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=passw)
                user.save()
                u = User.objects.get(id=user.id)
                profile = Profile(gender=gender,address=address,contact=contact,image=image,user=u)
                profile.save()
                return redirect('log_in')
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'guest.html',context)


# ------------ login -------------
def log_in(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['passw']
        user = auth.authenticate(username=uname,password=passw)
        request.session["uid"] = user.id
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username or password....')
            return redirect('log_in')
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'guest.html',context)

# ------------- logout -------------

def log_out(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('log_in')


def home(request):
    if "uid" in request.session:
        category = Category.objects.all()
        context = {'category':category}
        return render(request,'home.html',context)
    else:
        return redirect('log_in')

def cart(request,pk):
    if "uid" in request.session:
        if request.method == 'POST':
            pname = request.POST['pname']
            brand = request.POST['brand']
            category = request.POST['category']
            price = request.POST['price']
            user = request.session["uid"]
            pid = Product.objects.get(id=pk)
            cart = Cart(product_name=pname,product_price=price,user_id=user,brand_name=brand,category_name=category,product=pid)
            cart.save()
            return redirect('show_cart')
    else:
        messages.info(request,'Login to add products to cart...!')
        return redirect('log_in')

def show_cart(request):
    if "uid" in request.session:
        user = request.session["uid"]
        item = Cart.objects.filter(user=user)
        # image = Product.objects.filter(id=item)
        context = {'item':item}
    return render(request,'cart/show_cart.html',context)




    
