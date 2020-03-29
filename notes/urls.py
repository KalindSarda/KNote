
from django.contrib import admin 
from django.urls import path 
from knote import views 
from django.conf.urls import url

urlpatterns = [ 
    
    path('', views.index, name="todo"), 
    
    path('del/<item_id>', views.delete, name="del"), 
    
    path('admin/', admin.site.urls), 
]

