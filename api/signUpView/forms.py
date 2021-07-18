from django.forms import ModelForm
from .models import Profile
from django import forms


class SignUpForm(ModelForm):
    profile_username = forms.CharField(label="Username", max_length=64, widget=forms.TextInput(attrs={'class': 'input',
                                                                                                      'placeholder': 'Mitko123 '
                                                                                                      }))
    profile_email = forms.EmailField(label="Email", max_length=128, widget=forms.EmailInput(attrs={'class': 'input',
                                                                                                   'placeholder': 'mitko123@adatapro.bg '
                                                                                                   }))
    password_hash = forms.CharField(label='Password', max_length=256, widget=forms.PasswordInput({'class': 'input',
                                                                                                  'placeholder': '********',
                                                                                                  }))

    class Meta:
        model = Profile
        fields = ["profile_username", "profile_email", "password_hash"]
