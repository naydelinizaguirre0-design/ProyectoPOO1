from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
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


@api_view(["GET", "PATCH", "DELETE"])
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsersViewSet(viewsets.ModelViewSet):
    model = Users
    serializer_class = UsersSerializer 

    def get_queryset(self):
        return Users.objects.all()
