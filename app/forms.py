from django import forms
from .models import Product,Category,Register,Comment,ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nomi','batafsil','narxi','category']

    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class' : 'form-control'})
    

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['rasm','username' , 'first_name' , 'last_name', 'email' ,'number','adress','password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)