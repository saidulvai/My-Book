from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bios = models.TextField()
    image = models.ImageField(upload_to='author/image')
    social_media_links = models.URLField(blank=True)

    def __str__(sefl):
        return sefl.user.username