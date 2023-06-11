from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy

class UserManager(BaseUserManager):
    '''Manager class for the user model'''

    def create_user(self, username, email, password, **extras):
        '''Function to handle creating the user'''

        # check if the user put in email and username values
        if not email:
            raise ValueError(gettext_lazy('Email field is required'))
        
        if not username:
            raise ValueError(gettext_lazy('Username field is required'))
        
        email = self.normalize_email(email)
        
        # create a new user object
        user = self.model(username=username, email=email, **extras)

        # set user password and save the user
        user.set_password(password)
        user.save()

        # return user object
        return user
    
    def create_superuser(self, username, password, **extras):
        '''Function to create a superuser'''

        # set default values
        extras.setdefault('is_superuser', True)
        extras.setdefault('is_active', True)
        extras.setdefault('is_staff', True)

        if extras.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser should have is_superuser set to True'))
        elif extras.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser should have is_staff set to True'))
        
        # create superuser
        return self.create_user(username, password, **extras)