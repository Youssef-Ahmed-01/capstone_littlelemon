from .models import Booking, Menu
from django.contrib.auth.models import User, Group
from rest_framework import  serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        customer_group, created = Group.objects.get_or_create(name='Customer')
        user.groups.add(customer_group)
        user.save()
        return user

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'
