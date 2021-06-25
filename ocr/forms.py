from django import forms

from .models import *

# Form for id card.
class IdCardForm(forms.ModelForm):
    class Meta:
        model = IDCard
        fields = ["image"]
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "drop-zone__input",
                }
            )
        }


# Form for student card.
class StudentCardForm(forms.ModelForm):
    class Meta:
        model = Student_Card
        fields = ["image"]
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "drop-zone__input",
                }
            )
        }
