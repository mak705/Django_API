from .models import Stock
from rest_framework import serializers
from django.contrib.auth import get_user_model

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        #exclude = ('')
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
