from rest_framework import serializers
from .models import *
class Userserializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = user
  fields = ['id','url','first_name','last_name','username','Email','mobile_no','Address','gender','age']