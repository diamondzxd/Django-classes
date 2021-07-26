from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import StudentModel
from .serializers import *
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def students(request):
	if(request.method=='GET'):
		s=StudentModel.objects.all().values()
		slist=list(s)
		return HttpResponse(slist)
	else:
		return HttpResponse('Invalid Request Method : Valid Option is GET')

@csrf_exempt
def addstudent(request):
	if(request.method=='POST'):
		data = JSONParser().parse(request)
		serializer = StudentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse("Record Updated Successfully")
		return HttpResponse('Record Saved')
	else:
		return HttpResponse('Invalid Request Method : Valid Option is POST')

@csrf_exempt
def deletestudent(request,id):
	if(request.method=='DELETE'):
		s=StudentModel.objects.get(id=id)
		s.delete()
		return HttpResponse('Record Deleted')
	else:
		return HttpResponse('Invalid Request Method : Valid Option is PUT')


@csrf_exempt
def updatestudent(request,id):
	if(request.method=='PUT'):
		s=StudentModel.objects.get(id=id)
		data = JSONParser().parse(request)
		serializer = StudentSerializer(s, data=data)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse("Record Updated Successfully")
	else:
		return HttpResponse('Invalid Request Method : Valid Option is DELETE')
