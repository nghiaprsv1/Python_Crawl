from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class Custumer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    selling_price = models.FloatField(null=True,blank=True)
    brand_name = models.CharField(max_length=200,null=True)
    discount_rate = models.FloatField(null=True,blank=True)
    current_seller = models.CharField(max_length=200,null=True)
    short_url = models.CharField(max_length=500,null=True)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class Shop(models.Model):
    current_seller = models.CharField(max_length=200,null=True)
    count = models.IntegerField()
    def __str__(self):
        return str(self.current_seller)

class Brand(models.Model):
    brand_name = models.CharField(max_length=200,null=True)
    count = models.IntegerField()
    def __str__(self):
        return str(self.brand_name)

