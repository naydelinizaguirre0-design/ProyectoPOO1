from django.urls import path, include
from rest_framework import routers 

from users.views import (
    get_user,
    create_user,
    get_users,
    user_detail,
    UsersViewSet
)

router = routers.DefaultRouter()
router.register(r"users2", UsersViewSet, "users") 

urlpatterns = [
    path("", include(router.urls)),
    path("users/example/", get_user, name="get_user_example"),
    path("create_user/", create_user, name="create_user"),
    path("users/", get_users, name="get_users"),
    path("user_detail/<int:pk>/", user_detail, name="user_detail")
]