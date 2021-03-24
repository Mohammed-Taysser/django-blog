from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text='This Value May Contain Only Letters, Numbers, And @/./+/-/_ Characters.')
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8, help_text='password must be greater than 8 char or more')
    password2 = forms.CharField(label=' repeat password', widget=forms.PasswordInput(), min_length=8, help_text='password must be greater than 8 char or more')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('password must be identical')
        return self.cleaned_data['password2']   # show under password 2

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('username already exist, please try another')
        return self.cleaned_data['username'] # show under username


class LoinForm(forms.ModelForm):
    username = forms.CharField(label='user name')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
