from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def form1(request):
	if(request.method=='GET'):
		return render(request,'filedemo/form1.html',None)
	else:
		p=Profile()
		p.name=request.POST.get('name')
		p.photo=request.FILES.get('photo')
		p.save()

		return HttpResponse(Profile.objects.values_list())


def display(request):
	profiles=Profile.objects.all()
	print("Succesfully Displayed!")
	return render(request,'filedemo/display.html',{'profiles':profiles})

def multi(request):
	if(request.method=='GET'):
		return render(request,'filedemo/multi.html',None)
	else:
		for f in request.FILES.getlist('photo'):
			p=Profile()
			p.name=request.POST.get('name')
			p.photo=f
			p.save()

		return HttpResponse(Profile.objects.values_list())