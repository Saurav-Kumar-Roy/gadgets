from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Products
from .models import Order
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request,"index.html",{'products':products})
    


def shop(request):
    products = Products.objects.all()
    return render(request,"shop.html",{'products':products})

def product(request):
     return render(request,"product.html")

def product(request,code):
    products = Products.objects.all()
    for product in products:
        if product.code == code:
            return render(request,"product.html",{'product':product})

def contact(request):
    return render(request,"contact.html")

def checkout(request):
    return render(request,"checkout.html")


def checkout(request,code):
    products = Products.objects.all()
    for product in products:
        if product.code == code:
            return render(request,"checkout.html",{'product':product})
            
def confirm(request):
    return render(request,"confirm.html")

def confirm(request,id):
    orders = Order.objects.all()
    for order in orders:
        if order.id == int(id):
            return render(request,"checkout.html",{'order':order})

def done(request):   
    try:
        email = request.POST['email']
        item_name = request.POST['item_name']
        item_price = request.POST['item_price']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        payment_method = request.POST['payment_method']
        transection_no = request.POST['transection_no']
        account_no = request.POST['account_no']
        delevary_address = request.POST['delevary_address']
        order = Order(email=email,item_name=item_name,item_price =item_price, first_name=first_name,last_name=last_name,payment_method=payment_method,transcetion_no=transection_no,account=account_no,delevary_address=delevary_address)
    except:
        print("error found")
        return render(request,'index.html')
    else:
        order.save()
        url1 = 'confirm.html'
        print("data saved")
        return render(request,url1,{'order':order})

def mail(request):
    return render(request,'home.html')

def send_gmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, subject, message)

        send_mail(
            subject,
            message,
            'sauravroy289@gmail.com',
            ['sauravroy288@gmail.com'],
            fail_silently= False,
        )
        return HttpResponseRedirect(reverse('index.html'))

    else:
        return HttpResponse("Invalid requeset")