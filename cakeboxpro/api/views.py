from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from api.serialiazers import Userserializer
# Create your views here.

class UsercreationView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
