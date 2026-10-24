from django.db import models


class Users(models.Model):

    class sexType(models.IntegerChoices):
        MALE = (1, "male")
        FEMALE = (2, "female")
        OTHER = (3, "other")
        
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=80)
    birth_day = models.DateField(null=False)
    password = models.CharField(max_length=10, blank=False, null=False)
    sex = models.IntegerField(choices=sexType.choices,
                            default=sexType.OTHER)
    phone = models.IntegerField()
