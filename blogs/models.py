from django.db import models
from django.contrib.auth.models import User
from author.models import author
# Create your models here.

RATING_CHOICES = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)
class categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    categories = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='categories')
    
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    


    def __str__(self):
        return self.title
    

class Rating(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('blog', 'user')
    
    def __str__(self) -> str:
        return f"{self.blog.title} - Rating: {self.rating}"
 
