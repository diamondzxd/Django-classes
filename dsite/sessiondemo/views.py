from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def AddSession(request):
	request.session['name']='Piyush'
	return HttpResponse("Session Created Succesfully!")

def ReadSessionData(request):
	name=request.session['name']
	return HttpResponse("Your Name is :- " + str(name))

def DeleteSession(request):
	del request.session['name']
	return HttpResponse('Session Data Deleted Succesfully!')

def Questions_home(request):
	questions=[
	'In which continent is India country situated?',
	'Which country is the South Neighbour of India?',
	'What is the name of the Ocean named after India?',
	'Which is the coldest State of India?',
	'How many states does India have?'
	]

	options=[
		['Asia','North America','Australia','Europe'],
		['Sri Lanka','Pakistan','Nepal','Bangladesh'],
		['Pacific Ocean','Indian Ocean','Carribean Ocean','Antartic Ocean'],
		['Delhi','Karnataka','Telangana','Jammu & Kashmir'],
		['26','25','12','4']
	]

	request.session['questions']=questions
	request.session['options']=options
	request.session['index']=0
	return render(request,'sessiondemo/question_home.html',None)

def Questions_main(request):
	index=request.session['index']
	

	if(request.method=='POST'):
		if(request.POST.get('command')=='Next'):
			index=index+1
		elif(request.POST.get('command')=='Previous'):
			index=index-1
		else:
			#Dispose Session and Redierct to Result Page
			pass

	request.session['index']=index

	total=len(request.session['questions'])
	question=request.session['questions'][index]
	option=request.session['options'][index]



	return render(request,'sessiondemo/question_main.html',{'qno':index+1,'question':question,'option':option,'total':total})