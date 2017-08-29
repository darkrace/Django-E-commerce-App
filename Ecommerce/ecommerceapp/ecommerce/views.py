
from __future__ import unicode_literals
from django.template import Context
from django.shortcuts import render ,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout , get_user_model
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Registration
from .models import Product , PProduct
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request ):  
    return render(request , 'index.html' )
@login_required
def about(request):    
    return render(request ,'about.html' )
@login_required
def contact(request):   
    return render(request ,'contact.html' )
def single(request):   
    return render(request ,'single.html' )
def mens(request): 
    p = PProduct.objects.all()  
    return render(request ,'mens.html' , {'p': p})
def UserFormView(request):
	if request.method == 'POST':
		Name = request.POST.get('Name')
		Password = request.POST.get('Password')
        Item_Obj = Registration(Name = Name, Password = Password )
        Item_Obj.save()
        return HttpResponseRedirect('/index.html')

def Login(request):
    title = "Login"
    Names = request.POST.get('Name')
    Passwords = request.POST.get('Password')
    Registration.objects.all()
    x = Registration.objects.get(Name = Names , Password =Passwords)
    if x.Name == Names:
        return render(request , "index.html" , {'x':x})
    else:
        return render(request , "index.html" )

def Logout(request):
    request.session.flush()
    return render(request , "index.html")

def Image (request):
    Name = request.POST.get('Name')
    PName = request.POST.get('PName')
    Price = request.POST.get('Price')
    Item = request.POST.get('Item')
    Image = request.POST.get('Image')
    PK = Registration.objects.get(pk=Name)
    Item_Obj = Product(PName = PName, Price = Price , Item = Item , Image = Image , Name = PK )
    

    Item_Obj.save()
    return HttpResponseRedirect('/index.html')
