from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		#fields=['id','name','gender','age','city']
		fields='__all__'

	genderoptions=(
			('Male','Male'),
			('Female','Female'),
		)

	gender=forms.ChoiceField(choices=genderoptions, widget=forms.RadioSelect)

	cityoptions=(
			(1,'New Delhi'),
			(2,'Mumbai'),
			(3,'Chennai'),
			(4,'Gurugram')
		)

	city=forms.ChoiceField(choices=cityoptions)