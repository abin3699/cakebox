from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet

from api.serialiazers import Userserializer,Cakeserializer
from cakebxapp.models import Cakes
# Create your views here.

class UsercreationView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class Cakesview(ModelViewSet):
    serializer_class=Cakeserializer
    model=Cakes
    queryset=Cakes.objects.all()