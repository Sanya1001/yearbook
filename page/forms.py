from django import forms
from .models import Page, Stream


choices = Stream.objects.all().values_list('stream', 'stream')
choice_list = []
for item in choices:
    choice_list.append(item)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['name',
                  'quote',
                  'image',
                  'stream',
                  'mail',
                  'phone']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'quote': forms.Textarea(attrs={'class': 'form-control'}),
                   'mail': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'stream': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
                   }

