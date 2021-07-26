from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=20)
	desc=models.TextField()


class Brand(models.Model):
	name=models.CharField(max_length=20)
	logo=models.FileField()

class Product(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
	name=models.CharField(max_length=20)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	stock=models.IntegerField()