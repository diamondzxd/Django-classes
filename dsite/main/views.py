from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def Index(request):
	return HttpResponse("Hello World")

def Page1(request):
	return HttpResponse("Hello World")


def Page2(request):
	output='''
			<html>
				<head>
				</head>
				<body>
				<h1>Hello World</h1>
				</body>
				</html>
			'''
	return HttpResponse(output)

def Page3(request):
	return render(request,'page3.html',None)		#render(request,template,data)	

def Page4(request):
	return redirect('https://google.co.in/')


def Page5(request):
	data={}

	data['name']="Ravi Kumar"				#String
	data['age']=32							#Integer
	data['married']=True					#Boolean
	data['skills']=['C','C++','Java']		#List
	data['address']={'hno':'5','city':'Delhi'}	#Dictionary

	return render(request,'page5.html',data)

def Page6(request):
	data={'login':False}
	return render(request,'page6.html',data)



def Page7(request):					#Passing data to make a List in HTML
	data={'skills':['C','C++','Java','Python','Django']}
	return render(request,'page7.html',data)

def Page8(request):					#Passing data to make a table in HTML
	persons=[]
	persons.append({"name":"Piyush","email":"dhall.piyush@gmail.com"})
	persons.append({"name":"Ajay","email":"ajay@gmail.com"})
	persons.append({"name":"Vinay","email":"vinay@gmail.com"})
	persons.append({"name":"Test","email":"test@gmail.com"})

	return render(request,'page8.html',{'persons':persons})


def Page9(request):
	return render(request,'page9.html',None)



#Processing Form Data (Using HTML Forms)
def form1(request):
	#Determining Request Method
	return render(request,'form1.html',{'method':request.method})


def form2(request):
	method=request.method

	if(method=='GET'):
		return render(request,'form2.html',{'method':method})
	else:
		firstname=request.POST.get('firstname')		#fetching FirstName
		lastname=request.POST.get('lastname')
		gender=request.POST.get('gender')
		email=request.POST.get('email')
		city=request.POST.get('city')

		#Manual Validation
		isvalid=True
		errors={}

		#Validating Text 
		if(firstname==""):
			isvalid=False
			errors['firstname']='FirstName is required'
		if(lastname==""):
			isvalid=False
			errors['lastname']='LastName is required'
		if(email==""):
			isvalid=False
			errors['email']='email is required'


		if(isvalid==True):
			return render(request,'form2.html',{'method':method,'firstname':firstname,'lastname':lastname,'email':email,'gender':gender,'city':city})
		else:
			return render(request,'form2.html',{'method':'GET','errors':errors})
