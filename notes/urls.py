
from django.contrib import admin 
from django.urls import path 
from knote import views 
from django.conf.urls import url

urlpatterns = [ 
    
    path('', views.index, name="note"), 
    
	path('del/<item_id>', views.delete, name="del"),

	path('edit/<item_id>', views.edit, name="edit"),
    
    path('admin/', admin.site.urls), 
]
