from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import *
from .models import *

# Create your views here.
def AddStudent(request):
	if(request.method=='GET'):
		form=StudentForm()
		return render(request,'modelformdemo/form.html',{'form':form})
	else:
		student=StudentForm(request.POST)
		student.save()
		return HttpResponse('Record Saved Successfully')


def DisplayStudent(request):
	students=Student.objects.all()

	for s in students:
		if(s.city=='1'):
			s.city='New Delhi'
		elif(s.city=='2'):
			s.city='Mumbai'

	return render(request,'modelformdemo/display.html',{'students':students})


def UpdateStudent(request,id=1):
	if(request.method=='GET'):
		form=StudentForm(instance=Student.objects.get(id=id))
		return render(request,'modelformdemo/form.html',{'form':form})
	else:
		student=StudentForm(request.POST,instance=Student.objects.get(id=id))
		student.save()
		return HttpResponse('Record Saved Successfully')

def DeleteStudent(request,id=1):
	try:	
		s=Student.objects.get(id=id)
		s.delete()
		return HttpResponse('Record Deleted Successfully!')
	except:
		return HttpResponse('Invalid Data Entered!')