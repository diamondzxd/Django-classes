from django.db import models

# Create your models here.

class Order(models.Model):
	name=models.CharField(max_length=20)
	address=models.TextField()
	city=models.CharField(max_length=20)
	phone=models.IntegerField()
	pincode=models.IntegerField()
	state=models.CharField(max_length=20)
	product=models.CharField(max_length=30)
	price=models.IntegerField()