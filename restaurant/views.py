from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminOrManager, IsUer, IsManager, IsAdmin
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            customer_group = Group.objects.get(name='Customer')
            user.groups.add(customer_group)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
