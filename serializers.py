from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model
class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Task
        #fileds = ('id', 'task_name', 'task_desc')
        #exclude = ('id', 'task_name', 'task_desc')
        depth = 3
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    def create(self, validate_data):
        user = get_user_model().objects.create(username= validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
