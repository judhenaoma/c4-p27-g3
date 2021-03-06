from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_userhost(self, username, password, email, name, last_name):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            name= name,
            last_name= last_name
        )
        
        user.is_host = True
        user.is_houseHolder = False
        user.save(using=self._db)
    
    def create_user(self, username, password, email, name, last_name):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('El username es obligatorio')
        user = self.model(
            username=username, 
            email=email,
            name = name,
            last_name = last_name)
        user.set_password(password)
    
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.model(
            username=username,
            password=password
            )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_houseHolder = False
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', default= "NULL", max_length = 100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_name = models.CharField(max_length=30, null=True)
    born_date = models.DateField(null=True)
    is_host = models.BooleanField(default=False)
    is_houseHolder = models.BooleanField(default=True)

    # def save(self, **kwargs):
    #     some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
    #     self.password = make_password(self.password, some_salt)
    #     super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email
    