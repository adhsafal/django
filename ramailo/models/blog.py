from django.db import models
from ramailo.models.user import User
from ramailo.models.base import BaseModel

CATEGORY_CHOICES = [
    ('politics', 'Politics'),
    ('sports', 'Sports'),
    ('tech', 'Tech'),
    ('others', 'Others'),
]

class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name
    
class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.title}"
    
class PostImage(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='image')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.post.title}"