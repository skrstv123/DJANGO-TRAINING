from django import forms
from djangoapp.models import UserData
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		

class RegForm(forms.ModelForm):
	dob = forms.DateField(label='Date of Birth')
	choices = [
	('male','Male'),
	('female','Female'),

	]

	gender = forms.ChoiceField(choices=choices, widget= forms.RadioSelect)

	class Meta:
		model = UserData 
		fields = ('bio', 'gender', 'dob', 'location')


#-----------------------------------------
class post_form(forms.Form):
	head = forms.CharField(label = '',max_length=30,widget = forms.TextInput(attrs={
		'id':'head',
		'required':1,
		'placeholder':'enter head here......',
		'class':'head',
		})) 
	post = forms.CharField(label = '',max_length=3000,widget = forms.Textarea(attrs={
		'id':'post',
		'required':1,
		'placeholder':'write post here......',
		'class':'post',
		}))
