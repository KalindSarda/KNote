from django.shortcuts import render, redirect,get_object_or_404 
from django.contrib import messages   
from .forms import NoteForm 
from .models import KNote
from datetime import datetime
from dateutil.parser import *   
  
def index(request):

    item_list = KNote.objects.order_by("-title") 
    if request.method == "POST": 
        form = NoteForm(request.POST) 
        if form.is_valid(): 
            form.save()
            messages.info(request,"note added !!!")
            return redirect('note')

    form = NoteForm() 
  
    page = { 
             "forms" : form, 
             "list" : item_list, 
             "title" : "Note LIST", 
           } 
    return render(request, 'knote/index.html', page) 

def edit(request,item_id):
	item = KNote.objects.get(id=item_id)
	title = request.POST.get('edittitle')
	date = request.POST.get('editdate')
	details = request.POST.get('editdetails')
	fd =parse(date)
	item = KNote(id=item_id,title=title,details=details,date=fd)
	item.save()
	messages.info(request,"note updated !!!")
	return redirect('note')

		

def delete(request,item_id): 
    item = KNote.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "note removed !!!") 
    return redirect('note')
 
