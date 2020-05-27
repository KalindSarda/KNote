
from django import forms 
from .models import KNote
  
class NoteForm(forms.ModelForm): 
    class Meta: 
        model = KNote 
        fields="__all__"
