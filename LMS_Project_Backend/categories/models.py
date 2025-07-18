from django.db import models
from core.models.basse_model import BaseModel

# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=200 , unique=True, error_messages={"unique": "Category title already exists"})

    def __str__(self):
        return self.title
