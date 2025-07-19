from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models.basse_model import BaseModel

from django.core.exceptions import ValidationError

# Create your models here.


class CustomUser(BaseModel, AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(
        unique=True, error_messages={"unique": "Email already exists"}
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=128)

    class Role(models.TextChoices):
        STUDENT = "s", "Student"
        TEACHER = "t", "Teacher"
        ADMIN = "a", "Admin"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self):
        return f"{(self.username)--(self.role)}"
