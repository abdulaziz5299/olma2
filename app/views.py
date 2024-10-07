from django.shortcuts import render,redirect
from app.models import Product,Register,Category
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

# @login_required(login_url='login')
def home(request):
    product = Product.objects.all()
    if request.GET.get('search'):
        id = request.GET.get('search')
        product = Product.objects.filter(category__id=id)
    categories = Category.objects.all()
    
    return render(request,'index.html',{'product':product, 'categories': categories})

    
# @login_required(login_url='login')
# def detail(request,id):
#     p = Product.objects.get(id=id)
#     comment = Comment.objects.all()
    

#     return render(request,'single-post.html',{ 'p' : p ,'comment':comment})


def detail(request,id):
    f = {'p' : Product.objects.get(id=id)}    
    
    if request.POST.get('reply'):
        reply = request.POST['reply']
        comment_id = request.POST['comment_id']
        com = Comment.objects.get(id=comment_id)
        Comment.objects.create(
            comment = reply,
            user = request.user,
            product = p
        )
    elif request.POST.get('comment'):  
        Comment.objects.create(
            comment = request.POST.get('comment'),
            user = request.user,
            product = p,
        )

    # g = Comment.objects.all()        
        return redirect('detail', p.id)
    return render(request,'single-post.html',f)



def category(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'form.html', {'form':form})            

def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST,files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            parol = form.cleaned_data['password']
            a.set_password(parol)
            a.save
            return redirect('home')
    return render(request,'form.html',{'form':form}) 


def Login(request):
	form =  LoginForm()
	if request.POST:
		form =  LoginForm(request.POST)
		if form.is_valid():
			a = request.POST.get('username')
			b = request.POST.get('password')
			d = authenticate( request , username = a , password = b )
			if d is not None:
				login(request,d)
				return redirect( 'home' )
	return render( request , 'login.html' , { 'form' : form } )


# @login_required(login_url='login')
def create(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('create_image',a.id)
    return render(request,'form.html',{'form':form})

def create_image(request,id):
    form = ProductImageForm()
    if request.POST:
        form = ProductImageForm(files=request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.product = Product.objects.get(id=id)
            c.save()
    b = 'Yana rasm joylamoqchimisiz'
    return render(request,'create.html',{'form':form, 'b':b}) 

def delete(request,id):
    a = Product.objects.get(id=id)
    b = {
        'obj':a
    }
    return render(request,'delete.html',b)

def ishonch(request,id):
    Product.objects.get(id=id).delete()
    return redirect('home')

def edit(request,id):
    elon = Product.objects.get(id=id)
    form = ProductForm(instance=elon)
    if request.POST:
        form = ProductForm(request.POST, instance=elon)
        if form.is_valid():
            form.save()
            return redirect('home')
        # elon.category = request.POST['category']
          
    return render(request , 'form.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect('login')
# Create your views here.
