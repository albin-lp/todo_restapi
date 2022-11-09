from django.shortcuts import render
from api.models import Todo
from django.contrib.auth.models import User
from api.serializers import UserSerializer,TaskSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class UserSignupView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class TaskView(ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=TaskSerializer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self,request,*args,**kwargs):
        all_Tasks=Todo.objects.filter(user=request.user)
        serilaizer=TaskSerializer(all_Tasks,many=True)
        return Response(data=serilaizer.data)
    # def get_queryset(self):
    #     return Todo.objects.filter(user=self.request.user)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task=Todo.objects.get(id=id)
        serializer=TaskSerializer(task,many=False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Todo.objects.get(id=id)
        serializer=TaskSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        task=Todo.objects.get(id=id)
        task.delete()
        return Response({"msg": "task deleted"})

    @action(methods=["GET"],detail=False)
    def get_active(self,request,*args,**kwargs):
        all_Tasks=Todo.objects.filter(user=request.user)
        

     