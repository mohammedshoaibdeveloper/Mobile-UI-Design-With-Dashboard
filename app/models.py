from django.db import models

# Create your models here.
class category(models.Model):
    cid=models.AutoField(primary_key=True)
    mobileappname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.mobileappname


class product(models.Model):
    pid= models.AutoField(primary_key=True)
    appname= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    price= models.FloatField(max_length=1000,default=0.0)
    

    def __str__(self):
        return self.appname

class appinfo(models.Model):
    sno = models.AutoField(primary_key=True)
    img1name= models.CharField(max_length=255,default="")
    img1=models.ImageField(upload_to='upload/',default="dummy.jpg")
    img2name= models.CharField(max_length=255,default="")
    img2=models.ImageField(upload_to='upload/',default="dummy.jpg")
    img3name= models.CharField(max_length=255,default="")
    img3=models.ImageField(upload_to='upload/',default="dummy.jpg")
    img4name= models.CharField(max_length=255,default="")
    img4=models.ImageField(upload_to='upload/',default="dummy.jpg")
    img5name= models.CharField(max_length=255,default="")
    img5=models.ImageField(upload_to='upload/',default="dummy.jpg")
    
    category= models.ForeignKey(category, on_delete=models.CASCADE)


    def __str__(self):
        return self.category.mobileappname 

class client(models.Model):
    name=models.CharField(max_length=255,default="")
    companyname=models.CharField(max_length=255,default="")
    email=models.CharField(max_length=255,default="")
    contact=models.IntegerField()
    message=models.TextField()
    appid=models.ForeignKey(appinfo, on_delete=models.CASCADE)
    appimg=models.ImageField(upload_to='upload/',default="")

    def __str__(self):
        return self.email