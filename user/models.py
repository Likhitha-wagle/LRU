from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Permission
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class UserManager(BaseUserManager):
    def create_user(self,name,email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have full name')
        if not email:
            raise ValueError('Users must have an email address')
       
        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),

        )
        user.is_active=True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name,email,password=password
            # email=self.normalize_email(email),
            # full_name=full_name
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser=True
        user.is_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
       
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        if self.is_admin:
            return True
        elif str(self.group)=="Product Manager":
            group = Group.objects.get(name=self.group)
            try:
                permissions = group.permissions.get(codename=perm.split('.')[1])
                return True
            except:
                return False
        else:
            return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        db_table = "users"

class Twitter(models.Model):
    name = models.CharField(max_length=200)
    tweet=models.CharField(max_length=200)
    
    class Meta:
        db_table = "twitter"