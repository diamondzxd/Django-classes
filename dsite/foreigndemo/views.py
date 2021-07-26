from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def AddCategory(request):
	if(request.method=='GET'):
		f=CategoryForm()
		return render(request,'addcategory.html',{'f':f})

	else:
		category=CategoryForm(request.POST)
		category.save()
		return HttpResponse("Form Submited Succesfully!")

def DisplayCategory(request):
	categories=Category.objects.all()
	return render(request,'displaycategory.html',{'categories':categories})

def AddProduct(request):
	if(request.method=='GET'):
		f=ProductForm()
		return render(request,'addproduct.html',{'f':f})

	else:
		try:
			f=ProductForm()
			product=Product()
			product.name=request.POST.get('name')
			product.category=Category.objects.get(id=request.POST.get('category'))
			product.brand=Brand.objects.get(id=request.POST.get('brand'))
			product.price=request.POST.get('price')
			product.stock=request.POST.get('stock')
			product.save()
			return render(request,'addproduct.html',{'f':f,'success':True})
		except Exception as e:
			return render(request,'addproduct.html',{'f':f,'error':e})
def DisplayProduct(request):
	categories=Product.objects.all()
	return render(request,'displayproduct.html',{'categories':categories})

def AddBrand(request):
	if(request.method)=='GET':
		f=BrandForm()
		return render(request,'addbrand.html',{'f':f})
	else:
		p=Brand()
		p.name=request.POST.get('name')
		p.logo=request.FILES.get('logo')
		p.save()
		return HttpResponse("Brand Added Succesfully!")

def DisplayBrand(request):
	brands=Brand.objects.all()
	return render(request,'displaybrand.html',{'brands':brands})