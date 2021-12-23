from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import User



# Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=256 , null = True , blank= True)
#     preference = models.CharField(max_length= 256 , null = True , blank= True)
#     email = models.EmailField(unique= True , null = True , blank = True)
#     country = models.CharField(max_length= 100 , default = 'in')
#     # date_joined = models.DateTimeField()



#     def __str__(self):
#         return f'{self.user.username}'   


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length= 100 , default = 'in')
    preference = models.CharField(max_length= 256 , null = True , blank= True)


    def __str__(self):
        return f'{self.user.username}'

