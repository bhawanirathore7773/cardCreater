from django import forms
from .models import Pak_IdCard,Balaji_IdCard


class PakCardForm(forms.ModelForm):
    class Meta:
        model = Pak_IdCard
        fields = ('name', 'father_name', 'gender', 'image')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'image_class'})
        }



class BalajiCardForm(forms.ModelForm):
    class Meta:
        model = Balaji_IdCard
        fields = ('name', 'father_name', 'course','dob','address','state','image','mobile')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'image_class'})
        }