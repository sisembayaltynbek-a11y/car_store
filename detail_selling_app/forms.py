from django.contrib.auth.models import User
from django import forms
from .models import Cars

class AddYourCar(forms.ModelForm):
    class Meta:
        model = Cars
        exclude = ('seller','slug',)
        fields = '__all__'

class SellerSignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100, label="Full Name")  # Add this if you want a name field
    phonenumber = forms.CharField(max_length=15)
    address = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        
        if User.objects.filter(username=cleaned_data.get('username')).exists():
            raise forms.ValidationError("Username already exists")
        
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            raise forms.ValidationError("Email already registered")
            
        return cleaned_data