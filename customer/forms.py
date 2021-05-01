from accounts.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password1 = forms.CharField(

		widget=forms.PasswordInput,
		# help_text=password_validation.password_validators_help_text_html(),
	)

	class Meta:
		model = User
		fields = ("first_name","last_name","email", "password1", "password2")


	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.user_type = 2
		if commit:
			user.save()
		return user


class UserLoginForm(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

