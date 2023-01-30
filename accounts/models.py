from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#헬퍼클래스
class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

#실제 모델이 상속받아 생성하는 클래스가 Abstract
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password1 = models.CharField(max_length=30,  null=False, blank=False,default='password1')
    password2 = models.CharField(max_length=30,  null=False, blank=False,default='password2')
    StudentID = models.CharField(max_length=30,  null=False, blank=False,default='StudentID')
    Department = models.CharField(max_length=30,  null=False, blank=False,default='Department')

    objects = UserManager()

    USERNAME_FIELD = 'email'

