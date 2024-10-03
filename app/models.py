from django.db import models
from django.contrib.auth.models import AbstractUser



class Register(AbstractUser):
    rasm = models.ImageField(upload_to='user/')
    number = models.CharField(max_length=20,null=True)
    adress = models.CharField(max_length=100,null=True)

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)    
    
    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    nomi = models.CharField(max_length=30)
    batafsil = models.TextField(null=True)
    narxi = models.CharField(max_length=10)
    # rasmi = models.ImageField(upload_to='productimage/',null=True,blank=True)
    # rasmi = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name = 'product_comment')
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,related_name='comment_replies',null=True)


    def __str__(self):
        return f'{self.user}'  



class ProductImage(models.Model):
    image = models.ImageField(upload_to='rasm')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')




