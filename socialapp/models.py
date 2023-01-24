from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class Myuser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)

class Photos(models.Model):
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    like=models.ManyToManyField(Myuser,related_name="like") 

    def __str__(self):
        return self.image

class Comments(models.Model):
    photo=models.ForeignKey(Photos,on_delete=models.CASCADE)
    User=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)



