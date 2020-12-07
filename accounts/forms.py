from django import forms
from django.contrib.auth.models import User
from .models import Profile

#class LoginForm(forms.Form):
    #username = forms.CharField()
    #password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password' )

        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': 'username...'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': 'Bukhosi'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': 'Bukhosi'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': 'Moyo'}),
            'email':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': 'bukhosi@symaxx.com'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control form-control-solid py-4', 'placeholder': '********'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4 ', 'placeholder': 'Bukhosi'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4 ', 'placeholder': 'Bukhosi'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4 ', 'placeholder': 'Moyo'}),
            'email':forms.TextInput(attrs={'class': 'form-control form-control-solid py-4 ', 'placeholder': 'bukhosi@symaxx.com'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

        widgets = {
            'date_of_birth':forms.DateTimeInput(attrs={'class': 'form-control form-control-solid py-4', 'type':'text'}),
            'photo':forms.FileInput(attrs={'class': 'form-control form-control-solid'}),
        }