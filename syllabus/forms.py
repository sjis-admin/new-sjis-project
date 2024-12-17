# forms.py
from django import forms
from .models import Syllabus

class SyllabusUploadForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['category', 'title', 'file', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg h-24'}),
            'file': forms.FileInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }