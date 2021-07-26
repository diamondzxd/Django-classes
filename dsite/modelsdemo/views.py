from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentSimpleForm1,IdForm

# Create your views here.

def AddRequest(request):
	s=Student()
	s.id=2
	s.name='Piyush'
	s.course='ACCP'
	s.fees=45000
	s.duration=16
	s.save()
	return HttpResponse('Submitted Succesfully!')


def DisplayRecord(request):
	students=Student.objects.values_list()
	return HttpResponse(students)


def DeleteStudent(request):
	id=1
	try:
		s=Student.objects.get(id=id)
		s.delete()
		return HttpResponse('Record Deleted Succesfully')
	except:
		return HttpResponse('No Record Found for the Specified Query')


def UpdateStudent(request):
	id=1
	try:
		s=Student.objects.get(id=id)
		s.name='Update Name'
		s.course='Update Course'
		s.save()
		return HttpResponse('Record Updated Succesfully')
	except:
		return HttpResponse('No Record Found for the Specified Query')


def form1(request):
	method=request.method
	if(method=='GET'):
		data={}
		data['f']=StudentSimpleForm1()
		return render(request,'modelsdemo/model_form1.html',data)
	else:
		s=Student()
		s.id=request.POST.get('id')
		s.name=request.POST.get('name')
		s.course=request.POST.get('course')
		s.fees=request.POST.get('fees')
		s.duration=request.POST.get('duration')
		s.save()
		return HttpResponse("Data Submitted Succesfully!")

def DisplayRecordsAsTable(request):
	students=Student.objects.filter()
	return render(request,'modelsdemo/displayastable.html',{'students':students})

def DisplayRecordsAsGrid(request):
	students=Student.objects.filter()
	return render(request,'modelsdemo/displayasgrid.html',{'students':students})


def UpdateRecordForm(request):
	method=request.method
	if(method=='GET'):
		data={}
		data['f']=StudentSimpleForm1()
		return render(request,'modelsdemo/model_form1.html',data)
	else:
		try:
			id=request.POST.get('id')
			s=Student.objects.get(id=id)
			s.name=request.POST.get('name')
			s.course=request.POST.get('course')
			s.fees=request.POST.get('fees')
			s.save()
			return HttpResponse("Data Updated Succesfully!")
		except:
			return HttpResponse('No Record Found for the Specified Query')

def DeleteRecordForm(request,id):	
	method=request.method
	if(method=='GET'):
		data={}
		data['f']=IdForm()
		return render(request,'modelsdemo/delete_form.html',data)
	else:
		try:
			s=Student.objects.get(id=request.POST.get('id'))
			s.delete()
			return HttpResponse('Record Deleted Succesfully')
		except:
			return HttpResponse('No Record Found for the Specified Query')


def DeleteRecordForm2(request,id):	
	s=Student.objects.get(id=id)
	s.delete()
	return redirect('/modelsdemo/displayasgrid')


def UpdateRecordForm2(request,id):
	method=request.method
	if(method=='GET'):
		s=Student.objects.get(id=id)
		formcontent={
			'id':s.id,
			'name':s.name,
			'course':s.course,
			'fees':s.fees
		}
		data={}
		data['f']=StudentSimpleForm1(formcontent)
		return render(request,'modelsdemo/model_form1.html',data)
	else:
		try:
			s=Student.objects.get(id=id)
			s.name=request.POST.get('name')
			s.course=request.POST.get('course')
			s.fees=request.POST.get('fees')
			s.save()
			return redirect('/modelsdemo/displayasgrid')
		except Exception as e:
			return HttpResponse(e)