from django import forms
from .models import Category, Product, Brand

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		#fields=['id','name','desc']
		fields='__all__'


class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		#fields=['id','name','desc']
		fields='__all__'

	categories=tuple(Category.objects.values_list('id','name'))
	category=forms.ChoiceField(choices=categories)
	brands=tuple(Brand.objects.values_list('id','name'))
	brand=forms.ChoiceField(choices=brands)

class BrandForm(forms.ModelForm):
	class Meta:
		model=Brand
		fields=['name','logo']