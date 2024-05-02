from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder" : "Password"}))

    def confirm_login_allowed(self,user):
        if not user.is_active:
            raise forms.ValidationError("User is not active")
        return user

    def clean(self) :
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cashe = authenticate(self.request,username=username,password=password)
            if self.user_cashe:
                self.confirm_login_allowed(self.user_cashe)
            else:
                raise forms.ValidationError("Incorect login or password.")

        return self.cleaned_data     

        # if not User.objects.filter(username=username).exists():
        #     raise forms.ValidationError("User with this name does not exist.")
        # user = User.objects.get(username=username)
        # if user and not user.check_password(password):
        #     raise forms.ValidationError("Incorect password")
        # return self.cleaned_data

class RegisterForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" : "Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder" : "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder" : "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder" : "Password confirmation."}))


    class Meta:

        model = User
        fields = ("username","email")
        # widgets = {

        #     "username" : forms.TextInput(attrs={"class" : "form-control"}),
        #     "email" : forms.EmailInput(attrs={"class" : "form-control"}),
        #     "password1" : forms.PasswordInput(),
        #     "password2" : forms.PasswordInput()
        # }
    
        # labels = {
        #         "username" : 'Name',
                
        #         'email': 'Email',
        #     }
        # help_texts = {
        #         "username" : 'This field is required.',
                
        #         'email': 'This field is required.',
        #     }
        # error_messages = {
        #         "username" : {
        #             'required' :'This field is required.'
        #         },
                
        #         'email': {
        #             'required' : 'This field is required.'
        #         },
        #     }
        

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2
    

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user