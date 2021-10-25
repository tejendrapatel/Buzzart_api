from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .mypagenation import *

class userModelViewSet(ListAPIView):
    queryset = user.objects.all()
    serializer_class = Userserializer
    pagination_class = mylimitoffsetpagination

def SIGNUP(request):
    return render(request, "users.html")