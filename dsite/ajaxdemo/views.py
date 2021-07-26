from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json
from .models import Order
# Create your views here.

def BasicAjax(request):
	return render(request,'ajaxdemo/basicajax.html',None)

def BasicResponse(request):
	return HttpResponse("Jack & Jill went up the hill")

def BootStrapDemo1(request):
	return render(request,'ajaxdemo/bootstrapdemo.html',None)


def BootStrapDemo2(request):
	return render(request,'ajaxdemo/bootstrapdemo2.html',None)

def DisplayOrders(request):
	return render(request,'ajaxdemo/displayorders.html',None)


def FetchOrders(request):
	orders = serializers.serialize("json", Order.objects.all())
	data = {"orders": orders}
	return JsonResponse(data,safe=False)


@csrf_exempt
def AddOrder(request):
	if(request.method=='POST'):
		raw_data=json.loads(request.body)
		print(raw_data)
		o=Order()
		o.name=raw_data['name']
		o.address=raw_data['address']
		o.city=raw_data['city']
		o.phone=raw_data['phone']
		o.pincode=raw_data['pincode']
		o.state=raw_data['state']
		o.product=raw_data['product']
		o.price=raw_data['price']
		o.save()
		print("data saved Succesfully!")
		return HttpResponse("Submitted Data Succesfully!")