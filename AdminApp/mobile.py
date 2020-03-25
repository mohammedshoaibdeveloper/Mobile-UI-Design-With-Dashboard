from django.shortcuts import render,HttpResponse,redirect
from app.models import client,category,appinfo,SerClient
import json

# Create your views here.
def index(request):
    userdata=client.objects.all().order_by('-id')
    data={
        'userdata':userdata
    }
    return render(request,'dashboard/home.html',data)

def orders(request):
    userdata=client.objects.all().order_by('-id')
    data={
        'userdata':userdata
    }
    return render(request,'dashboard/orders.html',data)

def orderviews(request):
    userdata=client.objects.all().order_by('-id')
    serdata= SerClient(userdata, many=True)
    return HttpResponse(json.dumps(serdata.data))

def notifications(request):
    userdata=client.objects.filter(mark_time=0)
    serdata= SerClient(userdata, many=True)
    return HttpResponse(json.dumps(serdata.data))


def accept(request, id):
    data=client.objects.get(id=id)
    data.mark_time=1
    data.save()
    return redirect('/administrator')
