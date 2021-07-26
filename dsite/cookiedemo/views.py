from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def SaveCookie(reqeust):
	response=HttpResponse('Cookie Saved')
	response.set_cookie('name','Girish',max_age=60*60)
	return response


def ReadCookie(request):
	name=request.COOKIES.get('name')
	return HttpResponse("Welcome " + name)


def DeleteCookie(request):
	response=HttpResponse('Cookie Deleted')
	response.delete_cookie('name')
	return response


def CityPref(request):
	city=request.COOKIES.get('city')
	response=render(request,'cookiedemo/citypref.html',{'city':city})
	if(request.method=='POST'):
		response=redirect('/cookiedemo/citypref')
		if(request.POST.get('command')=='Save City'):
			response.set_cookie('city',request.POST.get('city'),max_age=3600*24*365)
		else:
			response.delete_cookie('city')
	return response

def cookiedemo_Home(request):
	login=request.COOKIES.get('login')
	response=render(request,'cookiedemo/cookiedemo_home.html',{'login':login})
	if login!=True:
		response.set_cookie('login',True,max_age=1000)
	return response


def cookiedemo_logout(request):
	response=redirect('/cookiedemo/cookiedemo_home')
	response.delete_cookie('login')
	return response