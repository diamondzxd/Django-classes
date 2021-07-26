from django import forms
from django.core.exceptions import ValidationError

#Simple Django Form
class StudentSimpleForm(forms.Form):
	id=forms.IntegerField()
	name=forms.CharField(max_length=40)
	course=forms.CharField(max_length=40)
	email=forms.EmailField()
	fees=forms.DecimalField(max_digits=10,decimal_places=2)



#Django Form - Using Widgets
class StudentSimpleForm2(forms.Form):
	citiesdata=(
			(0,'Select City'),
			(1,'New Delhi'),
			(2,'Chennai'),
			(3,'Kolkata')
		)

	genderdata=(
			(0,'Male'),
			(1,'Female')
		)

	preferencedata=(
			(0,'English'),
			(1,'Hindi'),
			(2,'Punjabi'),
			(3,'Urdu')


		)


	def validate_id(value):
		if(value<1 or value>100):
			raise ValidationError('Id must be between 1 to 100')

	def validate_name(value):
		if(len(value)<3):
			raise ValidationError('Minimum 3 Characters Required')


	id=forms.IntegerField(label="Enter Id", label_suffix=" ---> ", error_messages={'required':'Id is Required'}, validators=[validate_id])
	name=forms.CharField(max_length=40,validators=[validate_name],help_text='Minimum 3 Chacacters')
	gender=forms.ChoiceField(choices=genderdata,widget=forms.RadioSelect)
	course=forms.CharField(max_length=40)
	email=forms.EmailField(initial='admin@oldlappy.com')
	fees=forms.DecimalField(max_digits=10,decimal_places=2)
	city=forms.ChoiceField(choices=citiesdata)
	lang=forms.ChoiceField(choices=preferencedata,widget=forms.CheckboxSelectMultiple)
	photo=forms.FileField(required=False)
	dob=forms.DateField(required=False)
	newsletter=forms.BooleanField(label="Newsletter Subscription",required=False)

