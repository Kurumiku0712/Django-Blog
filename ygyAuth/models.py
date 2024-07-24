from django.db import models
from django.contrib.auth.models import User


class EmailCodeModel(models.Model):
    email = models.EmailField(unique=True)
    email_code = models.CharField(max_length=4)
    create_date = models.DateTimeField(auto_now_add=True)



