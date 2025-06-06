from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import CustomUser, Profile
from django.contrib.auth import get_user_model

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['fullName', 'email', 'password1', 'password2']
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'autocomplete': 'off',
            'readonly': 'true',
            'onfocus': 'this.removeAttribute("readonly");'
            })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'off',
            'readonly': 'true',
            'onfocus': 'this.removeAttribute("readonly");'
            })
    )
    
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tell us about yourself...'
            }),
        }


User = get_user_model()
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fullName', 'email']
