from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions

from api.serialiazers import Userserializer,Cakeserializer,Cartserializer
from cakebxapp.models import Cakes,Cake_variant,Cart
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
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    serializer_class=Cakeserializer
    model=Cakes
    queryset=Cakes.objects.all()

    @action(methods=["post"],detail=True)
    def cart_add(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        variant_obj=Cake_variant.objects.get(id=vid)
        user=request.user
        serializer=Cartserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Cake_variant=variant_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
