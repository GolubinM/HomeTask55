from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = PaperModels
        fields = ['title', 'description', 'image', 'upload', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 15}),
        }
