from django import forms
from .models import Funiture, Room

class AddRoomForm(forms.ModelForm): 

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': False
        })
        )
     
    class Meta:
        model = Room
        fields = ['room_type','image','theme']
        widgets = {
            
            'room_type': forms.Select(attrs={
                                        
            }),

            'theme': forms.Select(attrs={
                                        
            }),

            
        }


class UpdatePriceForm(forms.ModelForm): 

    object_price = forms.FloatField()
     
    class Meta:
        model = Funiture
        fields = ['object_price']


class UpdateImageForm(forms.ModelForm):

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': False
        })
        )

    class Meta:
        model = Room
        fields = ['image']
    