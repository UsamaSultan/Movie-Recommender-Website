from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import PasswordInput


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','first_name','last_name')
        
        widgets={
                   "username":forms.TextInput(attrs={'placeholder':'Username','class':'form-control', 'id':'Username-signup'}),
                   "email":forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            "first_name":forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            "last_name":forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
           
                  
                } 
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
   
        
        

    
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name')