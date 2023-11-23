from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address should be entered')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser should be is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser should be is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    """
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False):
        
        Creates and saves a User with the given email and password.
        
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        
        Creates and saves a staff user with the given email and password.
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
"""
"""
    def create_superuser(self, email, password):
        
        Creates and saves a superuser with the given email and password.
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(_(max_length=50), unique=True)
    email = models.EmailField(_('email address'), unique=True)
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    dateofbrth = models.DateField
    password = models.CharField(max_length=50)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
"""
class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'