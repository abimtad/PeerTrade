from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Your username',
		'class': 'w-full py-4 px-4  border-b-2 border-gray-300 rounded-xl',
	}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': 'w-full py-4 px-4  border-b-2 border-gray-300 rounded-xl',
	}))


class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
			'username': forms.TextInput(attrs={
				'placeholder': 'Username',
				'class': 'w-full py-4 px-4  border-b-2 border-gray-300 rounded-xl',
			}),
			'email': forms.EmailInput(attrs={
				'placeholder': 'Email',
				'class': 'w-full py-4 px-4 border-b hover:border-b-pink rounded-xl',
			}),
		}

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': 'w-full py-4 px-4 border-b hover:border-b-pink rounded-xl',
	}))

	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Repeat password',
		'class': 'w-full py-4 px-4 border-b hover:border-b-pink rounded-xl',
	}))