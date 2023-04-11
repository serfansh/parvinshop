from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs.update(
            { 'class': 'form-control'})
            
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control' })
            
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'})
            
        self.fields['email'].widget.attrs.update(
             {'class': 'form-control'})
            
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
            
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'form-control'})