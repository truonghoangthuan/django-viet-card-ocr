from django import forms

from .models import *


class IdCardForm(forms.ModelForm):
    class Meta:
        model = IDCard
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'drop-zone__input',
            })
        }
