from api.models import Todo
from django.contrib.auth.models import User
from  rest_framework import  serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]

    def create(self,validated_data):
          return User.objects.create_user(**validated_data)

class TaskSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    is_actve=serializers.BooleanField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Todo
        fields="__all__"

    def create(self,validated_data):
        user=self.context.get("user")
        return Todo.objects.create(**validated_data,user=user)