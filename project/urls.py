from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from app.views import home,create,register,category,Login,Logout,detail,create_image,delete,ishonch,edit
from django.conf import settings

from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('register/',register,name='register'),
    path('category/',category,name='category'),
    path('login/',Login,name = 'login'),
    path('logout/',Logout,name = 'logout'),
    path('detail/<int:id>',detail,name = 'detail'),
    path('create_image/<int:id>',create_image,name='create_image'),
    path('delete/<int:id>',delete,name='delete'),
    path('ishonch/<int:id>',ishonch,name='ishonch'),
    path('edit/<int:id>',edit,name='edit')






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
