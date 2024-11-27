from django.shortcuts import render
from .models import Invoice

# Create your views here.
def list(request):
    item=Invoice.objects.all
    return render(request,'myapp/list.html',{'item':item})

def accept(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        email=request.POST.get('email','')
        product=request.POST.get('product','')
        price=request.POST.get('price','')
        summary=request.POST.get('summary','')
        invoice=Invoice(name=name,phone=phone,address=address,email=email,product=product,price=price,summary=summary)
        invoice.save()

    return render (request,'myapp/accept.html')


