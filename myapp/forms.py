from django import forms
from .models import  Notebook




class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['brand', 'pages', 'size', 'type', 'price', 'description', 'story', 'author', 'cover_image']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Give a clear description...',
                'style': 'height:100px;'
            }),
            'story': forms.Textarea(attrs={
                'placeholder': 'Write the full story or notes here...',
                'style': 'height:150px;'
            }),
        }