from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializers 

user = {
    "name": "Naydelin",
    "password": "123"
}

@api_view(["GET"])
def get_user(requet)
    return Response(UsersSerializer(user).data)
