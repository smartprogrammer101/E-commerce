from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password and password2 and password != password2:
            raise ValidationError('Password does not match!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
         


class SignInEmailForm(forms.Form):
    email = forms.EmailField()

class SignInPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'error': 'password incorrect!'})


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs={
        'name':'name',
        'id':'name',
        'autofocus': True,
        }),
        error_messages={'error': 'something went wrong'}
    )
    email = forms.EmailField(min_length=3, max_length=50)
    password = forms.CharField(min_length=6, max_length=64, widget=forms.PasswordInput(attrs={
        'name':'password',
        'id':'password',
        'placeholder': 'at least 6 characters'
        })
    )
    password2 = forms.CharField(min_length=3, max_length=50, widget=forms.PasswordInput(attrs={
        'name':'password2',
        'id':'password2'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    # def check_password_match(self):
    #     c_data = self.cleaned_data
    #     if c_data['password'] != c_data['password2']:
    #         # raise ValidationErr('Passwords do not match!')
    #         self.password2 = forms.CharField(min_length=3, max_length=50, widget=forms.PasswordInput(attrs={
    #     'name':'password2',
    #     'id':'password2'
    #     }), error_messages={'passord do not match!'}
    # )
