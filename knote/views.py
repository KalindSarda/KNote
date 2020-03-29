from django.shortcuts import render, redirect,get_object_or_404 
from django.contrib import messages   
from .forms import TodoForm 
from .models import Todo  
  
def index(request): 
  
    item_list = Todo.objects.order_by("-title") 
    if request.method == "POST": 
        form = TodoForm(request.POST) 
        if form.is_valid(): 
            form.save()
            messages.info(request,"note added !!!")
            return redirect('todo') 
    form = TodoForm() 
  
    page = { 
             "forms" : form, 
             "list" : item_list, 
             "title" : "TODO LIST", 
           } 
    return render(request, 'knote/index.html', page) 
  
  
def delete(request,item_id): 
    item = Todo.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "note removed !!!") 
    return redirect('todo')
 