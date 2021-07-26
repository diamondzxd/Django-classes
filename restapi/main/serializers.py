from rest_framework import serializers
from main.models import StudentModel


class StudentSerializer(serializers.Serializer):    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False,max_length=50)
    course = serializers.CharField(required=False,max_length=50)
    duration = serializers.DecimalField(required=False,max_digits=10,decimal_places=2)


    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.course = validated_data.get('course', instance.course)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance