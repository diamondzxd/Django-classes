from django.shortcuts import render
from django.http import HttpResponse
from formsdemo.forms import *

# Create your views here.
def form1(request):
	#Unbound Form
	data={}
	data['f']=StudentSimpleForm()
	return render(request,'formsdemo/form1.html',data)



# Create your views here.
def form2(request):
	#Bounded Form

	formdata={}
	formdata['id']=1
	formdata['name']='Piyush'
	formdata['course']='Django'
	formdata['email']='piyush@mail.com'
	formdata['fees']=16000

	data={}
	data['f']=StudentSimpleForm(formdata)
	return render(request,'formsdemo/form2.html',data)

def form3(request):
	formdata={}
	data={}
	data['f']=StudentSimpleForm2(formdata)
	return render(request,'formsdemo/form3.html',data)


# Create your views here.
def form4(request):
	if(request.method=='GET'):
		#Bounded Form

		formdata={}
		formdata['id']=1
		formdata['name']='Piyush'
		formdata['course']='Django'
		formdata['email']='piyush@mail.com'
		formdata['fees']=16000
		formdata['gender']=0
		formdata['city']=2
		formdata['lang']=0

		data={}
		data['f']=StudentSimpleForm2(formdata)
		return render(request,'formsdemo/form3.html',data)
	
	else:
		#Form Validation

		f = StudentSimpleForm2(request.POST)

		if(f.is_valid()):
			return HttpResponse("Your Form Saved Successfully")
		else:
			data={}
			data['f']=f
			return render(request,'formsdemo/form3.html',data)
		

def form5(request):
		data={}
		data['f']=StudentSimpleForm2()
		return render(request,'formsdemo/form5.html',data)
