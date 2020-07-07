#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class cat(models.Model):
    cat_name=models.CharField(max_length=15)
    cat_icon = models.ImageField(upload_to='icon/', max_length=255 )
    cat_show =models.IntegerField()
    def __str__(self):
        return self.cat_name

class loc(models.Model):
    loc_name=models.CharField(max_length=30)
    def __str__(self):
        return self.loc_name
class ad(models.Model):
    ad_name=models.CharField(max_length=50)
    ad_posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    ad_price=models.FloatField()
    ad_loc = models.ForeignKey(loc,on_delete=models.CASCADE)
    img1= models.ImageField(upload_to='ad_img/', max_length=255 )
    img2= models.ImageField(upload_to='ad_img/', max_length=255)
    img3= models.ImageField(upload_to='ad_img/', max_length=255)
    img4= models.ImageField(upload_to='ad_img/', max_length=255)
    ad_des =models.CharField(max_length=1000)
    ad_cat=models.ForeignKey(cat,on_delete=models.CASCADE)
    ad_post_date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.ad_name

class message(models.Model):
    msg_regarding=models.CharField(max_length=25,null=True,blank=True)
    msg_content=models.CharField(max_length=150,null=True,blank=True)
    msg_ad=models.ForeignKey(ad,on_delete=models.CASCADE,null=True,blank=True)
    msg_from=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="sid")
    msg_to=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="rid")

    def __str__(self):
        return self.msg_content

class userprofile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=25,null=True,blank=True)
    firstname=models.CharField(max_length=25,null=True,blank=True)
    lastname=models.CharField(max_length=25,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=40,null=True,blank=True)
    profilepic=models.ImageField(upload_to='profile_pic/', max_length=255,null=True,blank=True)
    user_desc=models.CharField(max_length=25,null=True,blank=True)
    loc=models.CharField(max_length=25,null=True,blank=True)
    def __str__(self):
        return self.username