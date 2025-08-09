from django.db import models
from django.utils.text import slugify
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.author.fullName}"
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    liked_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together= ('user', 'post')
        
    def __str__(self):
        return f"{self.user} likes {self.post}"
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.user} commented on {self.post}"
    