from django.db import models

# Create your models here.
class StudentModel(models.Model):
	name=models.CharField(max_length=40)
	course=models.CharField(max_length=40)
	duration=models.DecimalField(max_digits=10,decimal_places=2)
