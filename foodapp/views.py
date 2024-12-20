from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        Contact.objects.create(name=name,email=email,phone=phone,message=message)
        messages.success(request,'Form sucessfully submitted!!!! ')
        return redirect('contact')
    return render(request,'food/home.html')


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        Contact.objects.create(name=name,email=email,phone=phone,message=message)
        messages.success(request,'Form sucessfully submitted!!!! ')
        return redirect('contact')
    
    return render(request,'food/contact.html')

def about_us(request):
    return render(request,'food/about_us.html')


def read(request):
    data=contact.objects.filter(Isdelete=False)
     
    return render(request,'food/read.html',{'data':data})


def delete(request,id):
    data=Contact.objects.get(id=id)
    data.Isdelete=True
    data.save()
    return redirect('read')

def update_form(request,id):
    data=Contact.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        data.name=name
        data.email=email
        data.phone=phone
        data.message=message
        data.save()
        return redirect('read')
    

    return render(request,'food/update_form.html',{'data':data})


def recycle(request):
    data=Contact.objects.filter(Isdelete=True)
     
    return render(request,'food/recycle.html',{'data':data})


def restore(request,id):
    data=Contact.objects.get(id=id)
    data.Isdelete=False
    data.save()
    return redirect('read')


from .models import Foods, Order
# from django.contrib.auth.decorators import login_required

def menu(request):
    data = Foods.objects.all()
    return render(request, 'food/menu.html', {'data': data})

# @login_required
def order_food(request, food_id):
    food = Foods.objects.get(id=food_id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        Order.objects.create(food=food, user=request.user, quantity=quantity)
        return redirect('order_success')
    return render(request, 'food/orders.html', {'food': food})