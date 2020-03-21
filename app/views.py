from django.shortcuts import render,HttpResponse,redirect
from .models import category,product,appinfo,client

# Create your views here.
def index(request):
    if request.method=="POST":
        appname=request.POST['appname']
        cat=request.POST['cat']
        
        price=request.POST['price']
        data=product(appname=appname,category=category.objects.get(mobileappname=cat),price=price)
        data.save()
        request.session['category'] = cat
       
   
        f=appinfo.objects.filter(category__mobileappname=cat)
       
     
        # return HttpResponse(f)
        
        return render(request,'index.html',{'data':f})
      
    data=category.objects.all()
    return render(request,'form.html',{'data':data})
    # return render(request,'form.html')

def detail(request,id):
    data=appinfo.objects.filter(sno=id)
    return render(request,'contact.html',{'data':data})


    
    
def mobile(request):
    return render(request,'index.html')
def contact(request):
    
    if request.method=="POST":
        name=request.POST['name']
        companyname=request.POST['companyname']
        email=request.POST['email']
        contact=request.POST['contact']
        message=request.POST['message']
        appid=request.POST['appid']
        data=client(name=name,companyname=companyname,email=email,contact=contact,message=message,appid=appid)
        data.save()
        if data:
            return redirect('https://mobileappstore.co.uk/')
    return HttpResponse('404')
    # return render(request,'contact.html')