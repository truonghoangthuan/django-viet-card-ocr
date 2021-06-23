from django import forms

from .models import *


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'drop-zone__input',
            })
        }
