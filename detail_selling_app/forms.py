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

    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=15)
    address = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data