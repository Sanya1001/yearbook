from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name',
                  'image',
                  'caption'
                  ]
        widgets = {'caption': forms.Textarea(attrs={'class': 'form-control'}),
                   'name': forms.TextInput(attrs={'class': 'form-control'})
                   }
