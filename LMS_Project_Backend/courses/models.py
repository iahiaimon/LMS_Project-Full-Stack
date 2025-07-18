from django.db import models
from core.models.basse_model import BaseModel
from accounts.models import CustomUser
from categories.models import Category

from django.core.exceptions import ValidationError

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=2)
    duration = models.DecimalField(decimal_places=2 , max_digits=2)
    teacher_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category , on_delete=models.CASCADE)

    def clean(self):
        if self.teacher.role != CustomUser.Role.TEACHER:
            raise ValidationError("Assigned user must have the role 'teacher'.")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title