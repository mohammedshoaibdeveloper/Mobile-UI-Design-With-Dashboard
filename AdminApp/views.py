from django.shortcuts import render,HttpResponse,redirect
from app.models import client,category,users,appinfo,SerClient,SerCategory
from django.contrib.sessions.models import Session 
from passlib.hash import pbkdf2_sha256
import json

# Create your views here.
def index(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    orders=client.objects.all().count()
    logos=appinfo.objects.all().count()
    catedata=category.objects.all().count()
    userdata=client.objects.all().order_by('-id')
    data={
        'userdata':userdata,
        'order':orders,
        'logos':logos,
        'catedata':catedata
    }
    return render(request,'dashboard/home.html',data)

def orders(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    userdata=client.objects.all().order_by('-id')
    data={
        'userdata':userdata
    }
    return render(request,'dashboard/orders.html',data)

# logos
def logos(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method =="POST":
        # title= request.POST['title']
        cate=category.objects.get(cid=request.POST['category'])
        img1name=request.POST['img1name']
        img1= request.FILES['img1']
        img2name=request.POST['img2name']
        img2= request.FILES['img2']
        img3name=request.POST['img3name']
        img3= request.FILES['img3']
        img4name=request.POST['img4name']
        img4= request.FILES['img4']
        img5name=request.POST['img5name']
        img5= request.FILES['img5']
        addlogo=appinfo(category=cate,img1name=img1name,img1=img1,img2name=img2name,img2=img2,img3name=img3name,img3=img3,img4name=img4name,img4=img4,img5name=img5name,img5=img5)
        addlogo.save()
        return redirect('logos')
    datas=appinfo.objects.all().order_by('-sno')
    cat=category.objects.all()
    data={
        'data':datas,
        'category':cat
        }
    return render(request,'dashboard/logos.html',data)


def logoupdate(request,id):
    if not request.session.has_key('userid'):
        return redirect('login')
    userdata=appinfo.objects.get(sno=id)
    ucat=category.objects.all()
    data={
        'data':userdata,
        'category':ucat
        }
    return render(request,'dashboard/updatelogos.html',data)

# update logo data
def updatelogodata(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method =="POST":
        id= request.POST['uid']
        cate=category.objects.get(cid=request.POST['category'])
        img1name=request.POST['img1name']
        img1= request.FILES['img1']
        img2name=request.POST['img2name']
        img2= request.FILES['img2']
        img3name=request.POST['img3name']
        img3= request.FILES['img3']
        img4name=request.POST['img4name']
        img4= request.FILES['img4']
        img5name=request.POST['img5name']
        img5= request.FILES['img5']
        data= appinfo.objects.get(sno=id)
        
        data.category=cate
        data.img1name =img1name
        data.img1 =img1
        data.img2name =img2name
        data.img2 =img2
        data.img3name =img3name
        data.img3 =img3
        data.img4name =img4name
        data.img4 =img4
        data.img5name =img5name
        data.img5 =img5
        data.save()
        return redirect('logos')
        
    
# Delete Logos
def deletelogo(request,id):
    if not request.session.has_key('userid'):
        return redirect('login')
    deletelogo=appinfo.objects.get(sno=id)
    deletelogo.delete()
    return redirect('logos')

# category 
def categoryview(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    return render(request,'dashboard/category.html')
# 
def categorydata(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    catdata= category.objects.all().order_by('-cid')
    alldata=SerCategory(catdata, many=True)
    return HttpResponse(json.dumps(alldata.data))


# category update data
def categoryupdatedata(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method =='GET':
        mydata=list()
        uid=request.GET['id']
        datas=category.objects.get(cid=uid)
        udata=SerCategory(datas)
        mydata.append(udata.data)
        return HttpResponse(json.dumps(mydata))
    elif request.method =='POST':
        uid=request.POST['uid']
        title=request.POST['utitle']
        data=category.objects.get(cid=uid)
        data.mobileappname=title
        data.save()
        return HttpResponse("success")

def categoryinsert(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method=="POST":
        title=request.POST['title']
        datas=category(mobileappname=title)
        datas.save()
        return HttpResponse('success')

# delete category
def delcategory(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method=="GET":
        id=request.GET['id']
        data=category.objects.get(cid=id)
        data.delete()
        return HttpResponse("success")

def orderviews(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    userdata=client.objects.all().order_by('-id')
    serdata= SerClient(userdata, many=True)
    return HttpResponse(json.dumps(serdata.data))

def notifications(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    userdata=client.objects.filter(mark_time=0)
    serdata= SerClient(userdata, many=True)
    return HttpResponse(json.dumps(serdata.data))


def accept(request, id):
    if not request.session.has_key('userid'):
        return redirect('login')
    data=client.objects.get(id=id)
    data.mark_time=1
    data.save()
    return redirect('/administrator')

# client message
def clientmessage(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    if request.method=="GET":
        msg = list()
        clientid=request.GET['id']
        msgdata=client.objects.get(id=clientid)
        mydata= SerClient(msgdata)
        msg.append(mydata.data)
        return HttpResponse(json.dumps(msg))

# settings
def settings(request):
    if not request.session.has_key('userid'):
        return redirect('login')

    if request.method=="POST":
        name=request.POST['uname']
        email=request.POST['uemail']
        password=request.POST['upassword']
        hashpwd=pbkdf2_sha256.hash(password)
        user=users.objects.get(userid=3)
        user.fullname=name
        user.email=email
        user.password=hashpwd
        user.save()
        return redirect('settings')
    data=users.objects.get(userid=3)
    return render(request,'dashboard/settings.html',{'data':data})
    # return render(request,'dashboard/settings.html')
    


# login 
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
       
        try:
             logindata=users.objects.get(email=email)
             if logindata:
                 
                if pbkdf2_sha256.verify(password,logindata.password):
                        request.session['userid']=logindata.userid
                        request.session['name']=logindata.fullname
                        return redirect('/administrator')
                else:
                    return redirect('login')
        except users.DoesNotExist:
            return redirect('login')

    return render(request,'dashboard/login.html')

# logout
def logout(request):
    if not request.session.has_key('userid'):
        return redirect('login')
    del request.session['userid']
    del request.session['name']
    return redirect('login')
