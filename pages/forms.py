from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Your login')
    password = forms.PasswordInput()
