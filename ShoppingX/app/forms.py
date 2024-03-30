from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class CustomRegistrationFrom(UserCreationForm):
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}) )
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))


from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _
from django.contrib.auth import password_validation

class MypasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old Password"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': 'True', 'class': 'form-control'}
        )
    )
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    new_password2 = forms.CharField(
        label="Confirm Password (again)",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=256, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))

class MySetPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    new_password2 = forms.CharField(
        label=_("Confirm Password (again)"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )