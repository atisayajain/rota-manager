

from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class MEMBER(models.Model):
    Member_name=models.CharField(max_length=20)
    Member_post=models.CharField(max_length=20)
    Membership_id=models.IntegerField()
    Roll_Number=models.CharField(max_length=8,default=timezone.now)
    Password=models.IntegerField()
    Email=models.TextField(max_length=30,default=timezone.now)
    Phone_Number=models.IntegerField(default=timezone.now)
    

    def __string__(self):
        return self.user
     

class RGM(models.Model):
    RGM_name=models.CharField(max_length=20)
    RGM_date=models.DateField()
    RGM_time=models.DateField()
    created_time=models.DateField(default=timezone.now)
    

    def __string__(self):
        return self.user


    

class Due(models.Model):
    Membership_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month_name=models.CharField(max_length=10)

    def __string__(self):
        return self.user

class Event_Detail(models.Model):
    Event_number=models.IntegerField()
    Event_name=models.CharField(max_length=100)

    def __string__(self):
        return self.user




    
