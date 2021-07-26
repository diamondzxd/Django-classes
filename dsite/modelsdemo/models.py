from django.db import models


class Student(models.Model):
	name=models.CharField(max_length=20)					
	course=models.CharField(max_length=20)					
	fees=models.DecimalField(max_digits=10,decimal_places=2)	
	duration=models.IntegerField(default=0)

'''
	create table modelsdemo_student(
		id int primary key,
		name varchar(20),
		course varchar(20),
		fees decimal(10,2)
	);
'''