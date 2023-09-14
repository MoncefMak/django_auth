from django.db import models

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = "SUPERADMIN", "SUPER ADMIN"
        STUFF = "STUFF", "STUFF"
        CUSTOMER = "CUSTOMER", "CUSTOMER"

    role = models.CharField(max_length=20, choices=Role.choices)

    # Add custom fields for all user types here

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users'
    )

