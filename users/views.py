from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsersSerializer 
from users.models import Users 

user = {
    "username": "Naydelin",
    "name": "Naydelin",
    "email" : "naydelin@mail.com",
    "password" : "123",
    "birth_day" : "22/09/2007",
    "phone" : "6981163969"
}

@api_view(["GET"])
def get_user(request):
    data = UsersSerializer(user).data
    birth = data['birth_day']


    return Response(data)



@api_view(["POST"])
def create_user(request):
    serialized_data = UsersSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_users(request):
    users = Users.objects.all()
    serialized_users = UsersSerializer(users, many=True)
    return Response(serialized_users.data)