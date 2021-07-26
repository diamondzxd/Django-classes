from django import forms
from django.core.exceptions import ValidationError

class StudentSimpleForm1(forms.Form):
	id=forms.IntegerField()
	name=forms.CharField(max_length=40)
	course=forms.CharField(max_length=40)
	fees=forms.DecimalField(max_digits=10,decimal_places=2)
	duration=forms.IntegerField()

class IdForm(forms.Form):
	id=forms.IntegerField()