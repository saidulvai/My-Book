from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from blogs.models import Blogs

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite {self.blog.title}"