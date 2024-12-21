from django.shortcuts import render,get_object_or_404,redirect
from .models import Invoice

# Create your views here.
def Item(request):
    pinaki=Invoice.objects.all()
    return render (request,"myapp/item.html",{'pinaki':pinaki})


def abc(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        address=request.POST.get("address","")
        phone=request.POST.get("phone","")
        price=request.POST.get("price","")
        description=request.POST.get("description","")
        pinaki=Invoice(name=name,address=address,phone=phone,price=price,description=description)
        pinaki.save()

    return render (request,"myapp/hello.html")


def update(request,id):
    sayan=get_object_or_404(Invoice,id=id)
    if request.method=="POST":
        sayan.name=request.POST.get("name","")
        sayan.address=request.POST.get("address","")
        sayan.phone=request.POST.get("phone","")
        sayan.price=request.POST.get("price","")
        sayan.description=request.POST.get("description","")
        sayan.save()
    return render (request,"myapp/update.html")


def delete(request,id):
    apple=get_object_or_404(Invoice,id=id)
    apple.delete()
    return redirect("myapp/item.html")








