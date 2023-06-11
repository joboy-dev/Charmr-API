from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    '''Custom User Model'''

    MALE = 'M'
    FEMALE = 'F'

    gender_choice = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    username = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=50, null=False, unique=True)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    profile_pic = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics', null=True)
    gender = models.CharField(choices=gender_choice, max_length=1, default=MALE, null=False)
    date_of_birth = models.DateField(null=False)
    age = models.IntegerField(default=0)
    height = models.DecimalField(null=False, decimal_places=2, max_digits=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    


