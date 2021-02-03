from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, Permission, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'email', 'password'
    ]

    email = models.EmailField(max_length=100)
    is_author = models.BooleanField(blank=True, null=True, default=False)
    is_admin = models.BooleanField(blank=True, null=True, default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name='Groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.',
        related_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User Permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="permissions",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = 'male', 'Male',
        FEMALE = 'female', 'Female',
        OTHER = 'other', 'Other'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GenderChoice.choices)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='users/', blank=True, null=True, default='users/avatar.png')
    city = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
