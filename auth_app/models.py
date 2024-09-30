from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
       ('Admin', 'Admin'),
        ('Author', 'Author'),
        ('Reader', 'Reader'),
)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.user_type}"
    



